#Convert distant given in feet and inches into meter and centimeter
ft = (int(input("Enter distance in feet :")))
inch = (int(input("Enter distance in inches:")))

# 1 foot = 0.3048 m
# 2 inches = 2.54 cm 

meter = ft * 0.3048 
cm = inch * 2.54 

print(f"Converted this {ft} feet distance into meter and answer is {meter}meter ")
print(f"Converted this {inch} inch distance into centimeter and answer is {cm}centimeter ")

