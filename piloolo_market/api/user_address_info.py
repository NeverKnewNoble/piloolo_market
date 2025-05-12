import frappe
import json


#! ~ Create and check user details 
@frappe.whitelist(allow_guest=True)
def save_user_address_info():
    import json

    data = frappe.local.form_dict

    # Extract from POST body
    username = data.get("username")
    address_data = data.get("address_data")

    if isinstance(address_data, str):
        address_data = json.loads(address_data)

    if not username or not address_data:
        frappe.throw("Missing username or address_data")

    existing = frappe.get_all("User Address Info", filters={"user": username}, limit=1)
    if existing:
        doc = frappe.get_doc("User Address Info", existing[0].name)
        doc.update(address_data)
        doc.save()
        frappe.db.commit()
        return {"message": "Address info updated", "data": doc}
    else:
        new_doc = frappe.get_doc({
            "doctype": "User Address Info",
            "user": username,
            **address_data
        })
        new_doc.insert()
        frappe.db.commit()
        return {"message": "Address info saved", "data": new_doc}



#! ~ Get user details
@frappe.whitelist(allow_guest=True)
def get_user_address_info(username):
    doc = frappe.get_all("User Address Info", filters={"user": username}, limit=1)

    if not doc:
        return {"message": "No address info found", "data": None}

    address_doc = frappe.get_doc("User Address Info", doc[0].name)
    return {
        "message": "Address info found",
        "data": address_doc.as_dict()
    }




# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.user_address_info.save_user_address_info
# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.user_address_info.get_user_address_info
