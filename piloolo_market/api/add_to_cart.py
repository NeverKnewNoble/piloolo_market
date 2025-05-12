import frappe
import json
from frappe.utils import now


#! ~ Create cart for user
@frappe.whitelist(allow_guest=True)
def add_to_cart(item_data, guest_id=None):
    if isinstance(item_data, str):
        item_data = json.loads(item_data)

    user = frappe.session.user
    is_guest = (user == "Guest")
    user_id = guest_id if is_guest else user

    if not user_id:
        frappe.throw("User ID or Guest ID is required", frappe.PermissionError)

    frappe.logger().info(f"Adding item for user_id: {user_id} (Guest: {is_guest})")

    # Check for existing open cart
    cart = frappe.get_all("Cart", filters={"user_id": user_id, "status": "Open"}, limit=1)

    if cart:
        cart_doc = frappe.get_doc("Cart", cart[0].name)
    else:
        cart_doc = frappe.get_doc({
            "doctype": "Cart",
            "user_id": user_id,
            "status": "Open",
            "order_items": []
        })
        cart_doc.insert(ignore_permissions=is_guest)

    # Calculate item_total
    quantity = int(item_data.get("quantity") or 0)
    price = float(item_data.get("item_price") or 0)
    item_total = quantity * price

    # Append item with item_total
    cart_doc.append("order_items", {
        "item": item_data["item"],
        "item_price": price,
        "size": item_data.get("size"),
        "quantity": quantity,
        "image_path": item_data.get("image_path"),
        "item_total": item_total
    })

    # Recalculate cart total
    total = sum(row.item_total or 0 for row in cart_doc.order_items)
    cart_doc.total = total

    cart_doc.save(ignore_permissions=is_guest)
    frappe.db.commit()

    return {
        "message": "Item added to cart",
        "cart_id": cart_doc.name,
        "cart_total": total
    }



#! ~ Call Cart Items for User
@frappe.whitelist(allow_guest=True)
def get_current_cart(guest_id=None):
    user = frappe.session.user
    is_guest = (user == "Guest")
    user_id = guest_id if is_guest else user

    if not user_id:
        frappe.throw("User ID or Guest ID is required", frappe.PermissionError)

    # Find the open cart for the user
    cart = frappe.get_all("Cart", filters={"user_id": user_id, "status": "Open"}, limit=1)
    if not cart:
        return {"message": "No open cart found", "cart": None}

    cart_doc = frappe.get_doc("Cart", cart[0].name)

    # Return cart details
    return {
        "message": "Open cart found",
        "cart_id": cart_doc.name,
        "user_id": cart_doc.user_id,
        "status": cart_doc.status,
        "order_items": cart_doc.order_items,
        "cart_total": cart_doc.total,
        "creation": cart_doc.creation,
        "last_modified": cart_doc.modified
    }



#! ~ Remove From Cart
@frappe.whitelist(allow_guest=True)
def remove_cart_item(index, guest_id=None):
    try:
        index = int(index)
    except ValueError:
        frappe.throw("Index must be an integer")

    user = frappe.session.user
    is_guest = (user == "Guest")
    user_id = guest_id if is_guest else user

    if not user_id:
        frappe.throw("User ID or Guest ID is required", frappe.PermissionError)

    # Find the open cart for the user
    cart = frappe.get_all("Cart", filters={"user_id": user_id, "status": "Open"}, limit=1)
    if not cart:
        frappe.throw("No open cart found")

    cart_doc = frappe.get_doc("Cart", cart[0].name)

    # Ensure the index is valid
    if index < 0 or index >= len(cart_doc.order_items):
        frappe.throw(f"Invalid index: {index}. Cart has {len(cart_doc.order_items)} item(s).")

    # Remove the item
    removed_item = cart_doc.order_items.pop(index)
    cart_doc.save()
    frappe.db.commit()

    return {
        "message": f"Item at index {index} removed successfully",
        "removed_item": removed_item.as_dict(),
        "remaining_items": [item.as_dict() for item in cart_doc.order_items],
        "cart_id": cart_doc.name
    }


# ! Clear cart
@frappe.whitelist(allow_guest=True)
def clear_cart(guest_id=None):
    user = frappe.session.user
    is_guest = (user == "Guest")
    user_id = guest_id if is_guest else user

    if not user_id:
        frappe.throw("User ID or Guest ID is required", frappe.PermissionError)

    # Find the open cart for the user
    cart = frappe.get_all("Cart", filters={"user_id": user_id, "status": "Open"}, limit=1)
    if not cart:
        return {"message": "No open cart found", "cart": None}

    cart_doc = frappe.get_doc("Cart", cart[0].name)

    # Clear all items in order_items table
    cart_doc.set("order_items", [])

    # Reset cart total
    cart_doc.total = 0.00

    # Save changes
    cart_doc.save(ignore_permissions=is_guest)
    frappe.db.commit()

    return {
        "message": "Cart has been cleared successfully",
        "cart_id": cart_doc.name,
        "remaining_items": [],
        "cart_total": 0.00
    }




# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.add_to_cart.add_to_cart
# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.add_to_cart.get_current_cart
# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.add_to_cart.remove_cart_item
# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.add_to_cart.clear_cart