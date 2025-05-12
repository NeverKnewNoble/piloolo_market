app_name = "piloolo_market"
app_title = "Piloolo Market"
app_publisher = "carbonitesolutions X Nortex"
app_description = "A ecommece app to support the piloolo mobile app"
app_email = "nortexnoble@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "piloolo_market",
# 		"logo": "/assets/piloolo_market/logo.png",
# 		"title": "Piloolo Market",
# 		"route": "/piloolo_market",
# 		"has_permission": "piloolo_market.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/piloolo_market/css/piloolo_market.css"
# app_include_js = "/assets/piloolo_market/js/piloolo_market.js"

# include js, css files in header of web template
# web_include_css = "/assets/piloolo_market/css/piloolo_market.css"
# web_include_js = "/assets/piloolo_market/js/piloolo_market.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "piloolo_market/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "piloolo_market/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "piloolo_market.utils.jinja_methods",
# 	"filters": "piloolo_market.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "piloolo_market.install.before_install"
# after_install = "piloolo_market.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "piloolo_market.uninstall.before_uninstall"
# after_uninstall = "piloolo_market.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "piloolo_market.utils.before_app_install"
# after_app_install = "piloolo_market.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "piloolo_market.utils.before_app_uninstall"
# after_app_uninstall = "piloolo_market.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "piloolo_market.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "piloolo_market.api.call_items.get_items",
#         "on_update": "piloolo_market.api.call_man_cloths.male_items",
#         "on_update": "piloolo_market.api.african_cloth.african_items",
# 		"on_update": "piloolo_market.api.women_cloth.female_items",

# 	}
# }

# hooks.py
doc_events = {
    "Doctype1": {
        "on_update": "piloolo_market.api.call_items.get_items"
    },
    "Doctype2": {
        "on_update": "piloolo_market.api.call_man_cloths.male_items"
    },
    "Doctype3": {
        "on_update": "piloolo_market.api.african_cloth.african_items"
    },
    "Doctype4": {
        "on_update": "piloolo_market.api.women_cloth.female_items"
    },
    "Doctype5": {
        "on_update": "piloolo_market.api.add_to_cart.add_to_cart"
    },
    "Doctype6": {
        "on_update": "piloolo_market.api.add_to_cart.get_current_cart"
    },
    "Doctype7": {
        "on_update": "piloolo_market.api.add_to_cart.remove_cart_item"
    },
    "Doctype8": {
        "on_update": "piloolo_market.api.user_address_info.save_user_address_info"
    },
    "Doctype9": {
        "on_update": "piloolo_market.api.user_address_info.get_user_address_info"
    },
    "Doctype10": {
        "on_update": "piloolo_market.api.feedback.submit_feedback"
    },
    "Doctype11": {
        "on_update": "piloolo_market.api.feedback.get_all_feedback"
    },
    "Doctype12": {
        "on_update": "piloolo_market.api.feedback.delete_feedback_by_index"
    },
    "Doctype13": {
        "on_update": "piloolo_market.api.cancel_order.cancel_order"
    },
    "Doctype14": {
        "on_update": "piloolo_market.api.add_to_cart.clear_cart"
    },
}



# Expose a REST API endpoint for creating orders
whitelisted_methods = [
    "piloolo_market.api.order_api.create_order",
    "piloolo_market.api.login.verify_login",
    "piloolo_market.api.user_api.sign_up",
    "piloolo_market.api.forgot_pass_api.send_password_reset",
    "piloolo_market.api.order_history.get_user_orders",
]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"piloolo_market.tasks.all"
# 	],
# 	"daily": [
# 		"piloolo_market.tasks.daily"
# 	],
# 	"hourly": [
# 		"piloolo_market.tasks.hourly"
# 	],
# 	"weekly": [
# 		"piloolo_market.tasks.weekly"
# 	],
# 	"monthly": [
# 		"piloolo_market.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "piloolo_market.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "piloolo_market.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "piloolo_market.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["piloolo_market.utils.before_request"]
# after_request = ["piloolo_market.utils.after_request"]

# Job Events
# ----------
# before_job = ["piloolo_market.utils.before_job"]
# after_job = ["piloolo_market.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"piloolo_market.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

