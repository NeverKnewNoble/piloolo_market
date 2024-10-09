import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def send_password_reset():
    # Extract 'email' from the request body
    email = frappe.form_dict.get('email')

    # Debug log to confirm the email is received
    frappe.logger().info(f"Email received for reset: {email}")

    # Check if email is provided
    if not email:
        return {"status": "error", "message": _("Please provide an email.")}

    # Check if the user exists in the system
    user_exists = frappe.db.exists("User", {"email": email})
    if not user_exists:
        return {"status": "error", "message": _("User does not exist.")}

    try:
        # Send the password reset email
        user = frappe.get_doc("User", user_exists)

        # Debug log to confirm user doc is loaded
        frappe.logger().info(f"User found for reset: {user.name}")

        # Send the password reset email
        user.reset_password(send_email=True)  # Ensure send_email=True to actually send the email

        # Commit any DB changes
        frappe.db.commit()

        # Debug log to confirm email sending attempt
        frappe.logger().info("Password reset email sent.")

        return {"status": "success", "message": _("Password reset email sent successfully.")}
    except Exception as e:
        # Log any error
        frappe.log_error(message=str(e), title="Password Reset Failed")
        return {"status": "error", "message": str(e)}



# API endpoint: http://127.0.0.1:8001/api/v2/method/piloolo_market.api.forgot_pass_api.send_password_reset
