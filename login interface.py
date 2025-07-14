###login form using conditions
### built in username and password

   
username = "admin"
password = "1234"


entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")


if entered_username == username:
    if entered_password == password:
        print("Login successful!")
    else:
        print("Incorrect password!")
else:
    print("Username does not exist!")
