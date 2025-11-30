#WAP to input all sides of triangle and check whether triangle is valid or not.

a = int(input("enter 1st sides of traingle :"))
b = int(input("Enter 2nd side of traingle :"))
c = int(input("Enter 3rd side of triangle :"))

if(a + b > c):
    if(a + c > b):
        if(b + c > a):
            print("Triagnle is valid ")
else:
    print("Print triangle is not valid .")
        


