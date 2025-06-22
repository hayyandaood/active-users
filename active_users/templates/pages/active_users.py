from frappe import _
import frappe
from active_users.active_users import get_active_users

def get_context(context):
    context.active_users = get_active_users()
    context.title = _("Active Users")
    return context

# active_users/www/active_users.html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    {{ include_style("/assets/active_users/css/active_users.css") }}
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Full Name</th>
                    <th>Email</th>
                    <th>Last Active</th>
                </tr>
            </thead>
            <tbody id="active-users-list">
                {% for user in active_users %}
                <tr>
                    <td>{{ user.full_name }}</td>
                    <td>{{ user.email }}</td>
                    <td>{{ user.last_active }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    {{ include_script("/assets/active_users/js/active_users.js") }}
</body>
</html>