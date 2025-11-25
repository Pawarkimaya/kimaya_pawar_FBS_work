#WAP to find the roots of quadratic equation
#ax**2+b*x+c=0
import math

a=(float(input("a:")))
b=(float(input("b:")))
c=(float(input("c:")))

D = (b*b)-(4*a*c)

root1 = (-b + math.sqrt(D)) / (2*a)
root2 = (-b - math.sqrt(D)) / (2*a)

print("Root 1 is :",root1)
print("Root 2 is :",root2)




