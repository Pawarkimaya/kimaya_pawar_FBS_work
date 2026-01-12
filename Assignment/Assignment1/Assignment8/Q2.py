def area(r):
    area=3.14 * r * r
    return area

r = float(input("Enter radius of circle:"))
res =  area(r)

print(f'Area of circle is {res}')