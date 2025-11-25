#Find the volume of sphere
r=(float(input("Enter radius of sphere:")))

r_cube = r * r * r

Volume = 4/3 * 3.14 * r_cube

print(f"Volume of sphere is {Volume:.2f}")