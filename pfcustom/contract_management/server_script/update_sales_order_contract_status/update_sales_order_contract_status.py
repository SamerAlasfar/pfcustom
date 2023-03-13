if doc.contract_type == 'Renewed Contract':
    frappe.db.set_value("Sales Order",doc.parent_contract,"contract_status","Renewed")