# 5. Write a program to find factorial using recursion.

def factorial(n):
    if n==1 or n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
    
    
    
n = int(input("Enter n:"))

result = factorial(n)

print("factorial of {n} is  : ",result)
