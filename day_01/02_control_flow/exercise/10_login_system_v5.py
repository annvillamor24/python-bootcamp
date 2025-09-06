# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")


admin_log_in = admin_username == username_input and admin_password==password_input
correct_user_log_in = username_input == correct_username and password_input==correct_password

# TODO: Notify user if credentials are valid or invalid


correct_credentials=admin_log_in or correct_user_log_in
if correct_credentials:
    print("Access Granted")
else:
    print("Access Denied")
