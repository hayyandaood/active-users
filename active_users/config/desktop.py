from frappe import _

def get_data():
	return [
		{
			"module_name": "Diamond Active Users",
			"color": "blue",
            "icon": "octicon octicon-person",
            "type": "link",
            "link": "/active-users",
			"label": _("Diamond Active Users")
		}
	]
