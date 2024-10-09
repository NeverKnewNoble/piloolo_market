import frappe

# ************API TO CALL MEN PRODUCTS IN USD******************
@frappe.whitelist(allow_guest=True)
def female_items(self=None, method=None):
    try:
        # Fetch items along with their price details, filtering by USD currency, 'Men' gender, and non-traditional wear
        items_with_usd_prices = frappe.db.sql("""
            SELECT 
                item.item_name,
                item.image,
                item.custom_gender,
                item.custom_women_category,
                item.custom_stock_on_site_status,
                price.currency,
                price.price_list_rate
            FROM 
                `tabItem` AS item
            LEFT JOIN 
                `tabItem Price` AS price ON item.item_name = price.item_name
            WHERE 
                price.currency = 'USD'
                AND item.custom_gender = 'Women'
                AND item.custom_is_traditional_wear_african_print = 0
                AND custom_stock_on_site_status = 'In Stock'
        """, as_dict=True)

        return {"data": items_with_usd_prices}  # Return the data in a proper format

    except Exception as e:
        # Handle error message
        frappe.log_error(frappe.get_traceback(), 'Get Items API Error')
        return {"error": str(e)}



#  http://127.0.0.1:8001/api/v2/method/piloolo_market.api.women_cloth.female_items
