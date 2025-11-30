#Write a program to check if user has entered correct userid and password.

userid =  input("Enter your userid :")
password = input("Enter your password :")

correct_userid = "kimaya"
correct_password = "12345"

if userid == correct_userid and password == correct_password:
    print("Login Successful!")
else:
    print("Invalid UserID or Password")