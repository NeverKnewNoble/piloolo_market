import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_order(order_data=None):
    try:
        # Ensure order_data is provided
        if not order_data:
            return {"status": "error", "message": _("Order data is required")}

        # Parse the input data (assuming JSON is passed)
        order_data = frappe.parse_json(order_data)
        
        # Create a new document for 'Orderings App'
        order_doc = frappe.get_doc({
            "doctype": "Orderings App",
            "total_amount": order_data.get("total_amount"),
            "shipping_fee": order_data.get("shipping_fee"),
            "usr_first_name": order_data.get("usr_first_name"),
            "usr_last_name": order_data.get("usr_last_name"),
            "location": order_data.get("location"),
            "city": order_data.get("city"),
            "phone_number": order_data.get("phone_number"),
            "stateprovidence_option": order_data.get("stateprovidence_option"),
            "postzip_code": order_data.get("postzip_code"),
            "address_line_1": order_data.get("address_line_1"),
            "address_line_2_optional": order_data.get("address_line_2_optional"),
            "email": order_data.get("email"),
            "currency": order_data.get("currency"),
            # You can add more fields as required
        })
        
        # Add items to the child table 'ordered Items'
        if "items" in order_data:
            for item in order_data["items"]:
                order_doc.append("items", {
                    "item": item.get("item"),
                    "item_price": item.get("item_price"),
                    "size": item.get("item_size"),
                    "quantity": item.get("item_quantity"), 
                })

        # Save the document
        order_doc.insert()
        frappe.db.commit()

        # Return success response
        return {"status": "success", "message": _("Order created successfully"), "order_name": order_doc.name}

    except Exception as e:
        frappe.log_error(message=str(e), title="Order Creation Failed")
        return {"status": "error", "message": str(e)}




# # http://127.0.0.1:8001/api/v2/method/piloolo_market.api.order_api.create_order