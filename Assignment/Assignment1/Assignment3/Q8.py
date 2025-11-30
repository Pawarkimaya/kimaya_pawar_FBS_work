'''Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)'''

import random

userid =  input("Enter your userid :")
password = input("Enter your password :")

correct_userid = "kimaya"
correct_password = "12345"

if (userid != correct_userid or password != correct_password):
    print("Invalid UserID or Password")
else:
    captcha = random.randint(1000,9999)
    print(captcha)
    userentercaptcha = int(input("Enter the same number that showing on the screen to know you are not robot :"))
    if(captcha == userentercaptcha):
        print("Successfully login done.")
    else:
        print("failed !!")

              
              

