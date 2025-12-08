#5. WAP to print Fibonacci series upto n.

n =  int(input("Enter number :"))
a = -1
b = 1

for i in range(n+1):
    c = a + b
    print(c,end = " ")
    a = b
    b = c