import frappe
import json

# ! Send feedback
@frappe.whitelist(allow_guest=True)
def submit_feedback():
    data = frappe.request.get_json()

    email = data.get("email")
    feedback = data.get("feedback")

    if not email or not feedback:
        frappe.throw("Both email and feedback are required")

    doc = frappe.get_doc({
        "doctype": "Feedback",
        "email": email,
        "feedback": feedback
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"message": "Feedback submitted successfully", "docname": doc.name}

# ! Get all feedback
@frappe.whitelist(allow_guest=True)
def get_all_feedback():
    feedback_docs = frappe.get_all(
        "Feedback",
        fields=["name", "email", "feedback", "creation"],
        order_by="creation desc"
    )
    return {"data": feedback_docs}

# ! Delete feedback
@frappe.whitelist(allow_guest=True)
def delete_feedback_by_index(index: int):
    index = int(index)
    all_feedback = frappe.get_all("Feedback", fields=["name"], order_by="creation asc")

    if index < 0 or index >= len(all_feedback):
        frappe.throw("Invalid index provided.")

    docname = all_feedback[index].name
    frappe.delete_doc("Feedback", docname, ignore_permissions=True)
    frappe.db.commit()

    return {"message": f"Feedback at index {index} deleted", "docname": docname}


# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.feedback.save_feedback
# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.feedback.get_all_feedback
# http://127.0.0.1:8001/api/method/piloolo_market.api.feedback.delete_feedback_by_index