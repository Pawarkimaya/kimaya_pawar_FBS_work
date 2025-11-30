#Write a program to input angles of a triangle and check whether triangle is valid or not.

name = input("Enter triangle name :")
#take input of triangles
a = int(input("Enter 1st angle of given triangle:"))
b = int(input("Enter 2nd angle of given triangle :"))
c = int(input("Enter 3rd angle of given triangle :"))

#A triangle is valid only in below condition 1.Sum of all three angles = 180°
#2. Each angle must be greater than 0°

if(a > 0 ):
    if(b > 0):
        if(c > 0):
            sum = a + b + c
            if(sum == 180):
                print(f"{name} triangle is valid .")
else:
    print("Triangle is not valid.")
