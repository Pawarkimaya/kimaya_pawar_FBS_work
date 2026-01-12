# 4. Write a program to find sum of n numbers using recursion.
def sum_of_series(n):
    if n==1 :
        return 1
    else:
        return n + sum_of_series(n-1)
    
    
    
    
n = int(input("Enter n:"))

result = sum_of_series(n)

print("Sum of series : ",result)
