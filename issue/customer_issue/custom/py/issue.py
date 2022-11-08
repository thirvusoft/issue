import frappe

def user_list(doc, actions):
    user_list = frappe.db.get_value("Project",{"name":doc.project})
    user_name = frappe.db.get_all("Project User",filters={"parent":user_list},fields=["user"])
    for i in user_name:
        if(not frappe.db.exists("Assignment Rule User",{
            "parent":"Issue",
            "parentfield":"users",
            "parenttype":"Assignment Rule",
            "user":i.user
        })):
            doc_ = frappe.new_doc("Assignment Rule User")

            doc_.update({
                "parent":"Issue",
                "parentfield":"users",
                "parenttype":"Assignment Rule",
                "user":i.user
            })
            doc_.save()

    new_doc = frappe.new_doc("Task")
    new_doc.update({
        "subject":doc.subject,
        "project":doc.project,
        "priority":doc.priority,
        "issue":doc.name,
        "description":doc.description
    })
    new_doc.flags.ignore_links = True
    new_doc.save(ignore_permissions = True)  

