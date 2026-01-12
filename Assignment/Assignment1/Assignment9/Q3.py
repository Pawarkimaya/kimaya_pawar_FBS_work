# 3. Write a program to reverse a given number using recursive function.


def reverse(n,rev=0):
    if n== 0  :
        return rev
    else:
        return reverse(n // 10, rev * 10 + n % 10)
    
    
    
n = int(input("Enter n:"))

result = reverse(n)

print("Sum of digits: " , result)