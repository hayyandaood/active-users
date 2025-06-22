import frappe

def get_active_users():
    """Fetch list of currently active users based on session data."""
    active_sessions = frappe.db.sql("""
        SELECT user, creation
        FROM `tabSessions`
        WHERE status = 'Active'
        ORDER BY creation DESC
    """, as_dict=True)
    
    users = []
    for session in active_sessions:
        user_info = frappe.get_doc("User", session.user)
        users.append({
            "full_name": user_info.full_name,
            "email": user_info.name,
            "last_active": session.creation
        })
    return users