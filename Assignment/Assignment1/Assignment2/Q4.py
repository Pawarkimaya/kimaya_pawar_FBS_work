#WAP to calculate area of triangle and rectangle 

# Triangle area = 0.5 * base * height
# Rectangle area = Length * breadth 

#Traingle
base=(float(input("Enter base of triangle:")))
height=(float(input("Enter height of triangle:")))

triarea = 1/2 * base * height

print(f"Area of triangle is {triarea}")

#Rectangle
length=(float(input("Enter length of rectangle :")))
breadth=(float(input("Enter breadth of rectangle  : ")))

recarea = length * breadth 

print(f"Area of rectangle is {recarea}")


