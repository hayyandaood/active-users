frappe.ready(() => {
    // Optional: Add client-side refresh functionality
    setInterval(() => {
        frappe.call({
            method: "active_users.active_users.get_active_users",
            callback: function(r) {
                if (r.message) {
                    let html = "";
                    r.message.forEach(user => {
                        html += `<tr>
                            <td>${user.full_name}</td>
                            <td>${user.email}</td>
                            <td>${user.last_active}</td>
                        </tr>`;
                    });
                    $("#active-users-list").html(html);
                }
            }
        });
    }, 60000); // Refresh every 60 seconds
});