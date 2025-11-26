#WAP to swap two number without using third variable

x=int(input("x :"))
y=int(input("y :"))

#1st method
#x,y = y,x3

#print("x :" ,x)
#print("y :" ,y)

#2nd method
y = x + y
x = y - x
y = y - x

print("x :" ,x)
print("y :" ,y)