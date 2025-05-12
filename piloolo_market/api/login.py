# import frappe
# from frappe import _
# from frappe import auth
# import secrets

# # ? --------------- API POST CALL TO CONFIRM LOGIN AUTHENTICATION ----------------------------
# @frappe.whitelist(allow_guest=True)
# def verify_login(username, password):
#     """Verify the user's login credentials."""
#     try:
#         # Check if the user exists
#         user = frappe.db.get_value("User", {"email": username})
#         if not user:
#             return {"status": "failed", "message": _("Invalid username")}

#         # Validate the credentials using Frappe's authenticate method
#         user_doc = frappe.get_doc("User", user)
#         if user_doc and frappe.utils.password.check_password(user_doc.name, password):
#             # If the credentials are valid, return success with full name
#             full_name = user_doc.full_name
#             return {"status": "success", "message": _("Login successful"), "full_name": full_name}
#         else:
#             return {"status": "failed", "message": _("Invalid password")}
    
#     except Exception as e:
#         return {"status": "error", "message": str(e)}
    

# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.login.verify_login


import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def verify_login(username, password):
    """Verify the user's login credentials and return full name and default currency."""
    try:
        # Check if the user exists
        user = frappe.db.get_value("User", {"email": username})
        if not user:
            return {"status": "failed", "message": _("Invalid username")}

        # Get the user document
        user_doc = frappe.get_doc("User", user)

        # Validate password
        if user_doc and frappe.utils.password.check_password(user_doc.name, password):
            # Fetch associated Customer record
            customer_currency = None

            # Try first by email_id
            customer = frappe.db.get_value("Customer", {"email_id": username}, ["name", "default_currency"], as_dict=True)

            # Fallback: try matching by full name if email_id is not set
            if not customer:
                customer = frappe.db.get_value("Customer", {"customer_name": user_doc.full_name}, ["name", "default_currency"], as_dict=True)

            if customer:
                customer_currency = customer.default_currency
            else:
                frappe.log_error(f"No customer found for user: {username}", "Customer Fetch Failed")

            return {
                "status": "success",
                "message": _("Login successful"),
                "username": username,
                "full_name": user_doc.full_name,
                "default_currency": customer_currency,
                "isLoggedIn": True
            }

        else:
            return {"status": "failed", "message": _("Invalid password")}

    except Exception as e:
        frappe.log_error(str(e), "Login Verification Error")
        return {"status": "error", "message": str(e)}

