import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_user_orders(self=None, method=None):
    try:
        # Get email from request parameters
        email = frappe.form_dict.get('email')
        
        if not email:
            return {"status": "error", "message": "Email parameter is required."}
        
        # Trim whitespace and ensure case consistency
        email = email.strip().lower()

        # Fetch orders created by the specified user
        orders = frappe.get_all('Orderings App',
                                filters={'email': email},
                                fields=['name', 'total_amount', 'shipping_fee', 'usr_first_name', 'usr_last_name', 'location', 'email', 'status'])

        # Log the filtered results for debugging
        frappe.logger().info(f"Filtered Orders: {orders}")

        # Retrieve the items from the child table for each order
        for order in orders:
            order_doc = frappe.get_doc('Orderings App', order['name'])
            order['items'] = [{
                "item": item.item,
                "item_price": item.item_price,
                "item_size": item.size,
                "quantity": item.quantity  # Assuming you have a quantity field in your items table
            } for item in order_doc.items]
        
        return {"status": "success", "orders": orders}

    except Exception as e:
        frappe.log_error(message=str(e), title="Fetching User Orders Failed")
        return {"status": "error", "message": str(e)}







# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.order_history.get_user_orders