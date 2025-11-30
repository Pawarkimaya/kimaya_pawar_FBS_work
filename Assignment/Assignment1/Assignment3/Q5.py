'''Write a program to check whether the triangle is equilateral, isosceles or scalene
triangle.'''
a = int(input("enter 1st side of traingle :"))
b = int(input("Enter 2nd side of traingle :"))
c = int(input("Enter 3rd side of triangle :"))

if(a + b > c):
    if(a + c >  b):
        if(b + c > a):
                if(a == b == c ):
                        print("It is an equilateral triangle.")
                else:
                    if(a ==b or b == c or a == c):
                        print("It is an Isosceles triangle.")
                    else:
                        print("It is an scalene triangle")
else:
     print("Triangle is not valid . ")

           





