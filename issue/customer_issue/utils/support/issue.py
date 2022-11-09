from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def issue_customization():
    issue_custom_field()
    issue_property_setter()

    
def issue_custom_field():
    issue_custom_fields = {
        "Issue": [
            dict(
                fieldname="ts_status",
                fieldtype="Data",
                label="Task Status",
                insert_after="customer",
                read_only = 1,
                in_list_view =1
            ),
        ],
    }
    create_custom_fields(issue_custom_fields)
def issue_property_setter(): 
    pass