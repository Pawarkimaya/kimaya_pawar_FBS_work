#WAP to input 2 angles from user and find third angle of the triangle
ABC=(str(input("Triangle name is:")))
angle1=(int(input("Enter angle1:",)))
angle2=(int(input("Enter angle2:")))

#apply formula 
angle3=180-angle1-angle2

print(f"Third angle of triangle{ABC} is {angle3}")
