# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

correct_username = username_input==correct_username
correct_password = password_input==correct_password

# TODO: Notify user if credentials are valid or invalid

if correct_username and correct_password:
    print("Access Granted")
else:
    print("Access Denied")
