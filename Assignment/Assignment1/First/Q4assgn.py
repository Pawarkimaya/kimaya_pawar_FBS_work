'''4. Calculate the cost of painting the following buildings walls (both interior and
exterior). You need to accept area (one wall) and cost of both interior and
exterior wall.
(Note: 1. Below diagram is of two joint rooms.
2. It is upper view of building.)'''

#area of one wall 
area = float(input("Enter area of one wall : "))

#painting cost
interior = float(input("interior paint cost per sq.m : "))
out = float(input("Exterior paint cost per sq.m : "))

interior_area = 8 * area
exterior_area = 7 * area

total_cost = (interior_area * interior) + (exterior_area * out )

print("Interior area =", interior_area)
print("Exterior area =", exterior_area)
print("Total cost =", total_cost)