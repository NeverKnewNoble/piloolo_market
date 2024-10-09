import frappe

# ************API TO CALL PRODUCTS IN USD******************
@frappe.whitelist(allow_guest=True)
def get_items(self=None, method=None):
    try:
        # Fetch items along with their price details, filtering only USD currency
        items_with_usd_prices = frappe.db.sql("""
            SELECT 
                item.item_name,
                item.image,
                item.custom_stock_on_site_status,
                price.currency,
                price.price_list_rate
            FROM 
                `tabItem` as item
            LEFT JOIN 
                `tabItem Price` as price ON item.item_name = price.item_name
            WHERE 
                price.currency = 'USD'
                AND custom_stock_on_site_status = 'In Stock'
                
        """, as_dict=True)

        return {"data": items_with_usd_prices}  # Return the data in a proper format

    except Exception as e:
        # Handle Error message
        frappe.log_error(frappe.get_traceback(), 'Get Items API Error')
        return {"error": str(e)}


#  http://127.0.0.1:8001/api/v2/method/piloolo_market.api.call_items.get_items
