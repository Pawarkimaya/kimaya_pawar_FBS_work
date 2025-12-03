#find the area and perimeter of figure
length = float(input("Enter length :"))
breadth = float(input("Enter breadth :"))
r = float(input("Enter radius :"))


rectangle_area = length * breadth
half_circlearea = 1 / 2 * 3.14 * r * r

total_area = rectangle_area + half_circlearea

total_peri = 2 * length + breadth * 3.14 * r

print("Area of following figure is ",total_area)
print("Perimeter of following figure is ",total_peri)



