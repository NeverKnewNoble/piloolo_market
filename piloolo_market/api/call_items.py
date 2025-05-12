import frappe

# ************API TO CALL PRODUCTS IN USD******************
# @frappe.whitelist(allow_guest=True)
# def get_items(self=None, method=None):
#     try:
#         # Fetch items along with their price details, filtering only USD currency
#         items_with_usd_prices = frappe.db.sql("""
#             SELECT 
#                 item.item_code,
#                 item.item_name,
#                 item.image,
#                 item.custom_stock_on_site_status,
#                 price.currency,
#                 price.price_list_rate
#             FROM 
#                 `tabItem` as item
#             LEFT JOIN 
#                 `tabItem Price` as price ON item.item_name = price.item_name
#             WHERE 
#                 price.currency = 'USD'
#                 AND custom_stock_on_site_status = 'In Stock'
                
#         """, as_dict=True)

#         return {"data": items_with_usd_prices}  # Return the data in a proper format

#     except Exception as e:
#         # Handle Error message
#         frappe.log_error(frappe.get_traceback(), 'Get Items API Error')
#         return {"error": str(e)}






# @frappe.whitelist(allow_guest=True)
# def get_items(self=None, method=None):
#     try:
#         # Step 1: Fetch items with USD price and in-stock status
#         items = frappe.db.sql("""
#             SELECT 
#                 item.item_code,
#                 item.item_name,
#                 item.image,
#                 item.custom_item_description,              
#                 item.custom_stock_on_site_status,
#                 price.currency,
#                 price.price_list_rate
#             FROM 
#                 `tabItem` AS item
#             LEFT JOIN 
#                 `tabItem Price` AS price ON item.item_name = price.item_name
#             WHERE 
#                 price.currency = 'USD' OR price.currency = 'GHS'
#                 AND item.custom_stock_on_site_status = 'In Stock'
#         """, as_dict=True)

#         # Step 2: For each item, fetch custom_sizes from child table
#         for item in items:
#             custom_sizes = frappe.get_all(
#                 "Product sizes", 
#                 filters={"parent": item["item_code"]},
#                 fields=["size", "status"]
#             )
#             item["custom_sizes"] = custom_sizes

#         return {"data": items}

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), 'Get Items API Error')
#         return {"error": str(e)}






@frappe.whitelist(allow_guest=True)
def get_items(currency=None):
    try:
        if currency not in ['USD', 'GHS']:
            return {"error": "Invalid or missing currency. Allowed: USD or GHS"}

        # Step 1: Fetch items with selected currency and in-stock status
        items = frappe.db.sql("""
            SELECT 
                item.item_code,
                item.item_name,
                item.image,
                item.custom_item_description,              
                item.custom_stock_on_site_status,
                price.currency,
                price.price_list_rate
            FROM 
                `tabItem` AS item
            LEFT JOIN 
                `tabItem Price` AS price ON item.item_name = price.item_name
            WHERE 
                price.currency = %s
                AND item.custom_stock_on_site_status = 'In Stock'
        """, (currency,), as_dict=True)

        # Step 2: For each item, fetch custom_sizes from child table
        for item in items:
            custom_sizes = frappe.get_all(
                "Product sizes", 
                filters={"parent": item["item_code"]},
                fields=["size", "status"]
            )
            item["custom_sizes"] = custom_sizes

        for feature in items:
            custom_product_features = frappe.get_all(
                "Product features", 
                filters={"parent": item["item_code"]},
                fields=["feature"]
            )
            item["custom_product_features"] = custom_product_features

        return {"data": items}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'Get Items API Error')
        return {"error": str(e)}




#  http://127.0.0.1:8001/api/v2/method/piloolo_market.api.call_items.get_items