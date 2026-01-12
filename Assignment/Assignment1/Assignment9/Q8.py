# 8. Write a program to check whether a number is prime or not using recursion.

def is_prime(n, i):
    if i == 1:                 
        return True
    if n % i == 0:             
        return False
    return is_prime(n, i - 1)  

num = int(input("Enter number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    if is_prime(num, num // 2):
        print("Prime Number")
    else:
        print("Not a Prime Number")
