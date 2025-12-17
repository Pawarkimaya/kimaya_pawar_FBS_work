# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
# 2. Enter number of students from user. For those many students accept marks of 5

# PART 1: User creates ID and Password
print("Create your Login Credentials:")
set_id = input("Set your user id: ")
set_password = input("Set your password :")

print("Your credentials are saved successfully!")
print("Now login...")

#part 2
for i in range(3):
    userid = input("Enter user id: ")
    password = input("Enter password: ")

    if userid == set_id and password == set_password :
        print("Login successfull!")
        break
    else:
        print("Incorrect!Try again.")
else:
    print("3 attempts over! Login failed.")