#WAP to swap two numbers using third variable
 
x=int(input("x :"))
y=int(input("y :"))

#with using third variable temp
temp = x

x = y 

y = temp


print("x:",x)
print("y:",y)