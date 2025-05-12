import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def cancel_order(order_name):
    try:
        # Ensure order_name is provided
        if not order_name:
            return {"status": "error", "message": _("Order name is required")}

        # Fetch the document from 'Orderings App' Doctype
        order_doc = frappe.get_doc("Orderings App", order_name)

        # Update the 'status' field to 'Cancelled'
        order_doc.status = "Cancelled"

        # Save and commit changes
        order_doc.save()
        frappe.db.commit()

        return {"status": "success", "message": _("Order cancelled successfully"), "order_name": order_name}

    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Order not found")}
    except Exception as e:
        frappe.log_error(message=str(e), title="Cancel Order Failed")
        return {"status": "error", "message": str(e)}


# http://127.0.0.1:8001/api/v2/method/piloolo_market.api.cancel_order.cancel_order