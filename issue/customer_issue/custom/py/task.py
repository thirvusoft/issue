import frappe

def on_update(doc, actions):
    get_issue = frappe.get_value("Issue",{"name":doc.issue})
    frappe.db.set_value("Issue",get_issue,"ts_status",doc.status)
