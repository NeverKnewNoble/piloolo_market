# piloolo_market/api/user_api.py
#  ! This api is to create a new user
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def sign_up(email, first_name, password):
    if not email or not first_name or not password:
        return {"status": "error", "message": _("Missing required fields.")}

    # Check if the user already exists
    if frappe.db.exists("User", {"email": email}):
        return {"status": "error", "message": _("User already exists.")}

    try:
        # Create new user
        user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": first_name,
            "enabled": 1,
            "new_password": password,
            "user_type": "Website User",
            "send_welcome_email": 0  # Set to 1 if you want to send a welcome email
        })
        user.flags.ignore_permissions = True  # Allow user creation without login
        user.insert()

        frappe.db.commit()

        # Ensure the correct response format
        return {"status": "success", "message": _("User created successfully.")}
    except Exception as e:
        frappe.log_error(message=str(e), title="User Registration Failed")
        return {"status": "error", "message": str(e)}


    
# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.user_api.sign_up
