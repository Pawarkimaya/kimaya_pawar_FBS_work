#

length = int(input("Enter length of field: "))
breadth = int(input("Enter breadth of field: "))
r = int(input("Enter radius of circle: "))
pi = 3.14

# perimeter of rectangle
rect_area = length * breadth + length * breadth

# circumference of circle
circle_para = pi * r

# total field measurement (just an example: rectangle area + circle circumference)
entire_field = rect_area + circle_para

costwire= entire_field / 35

# cost
total_cost = 5 * costwire

print("Entire field for per meter:", costwire)
print("Total cost for 5 times in rupees :", total_cost)
