# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms
# Function for sum: 1 + 2 + 3 + ... + n
def fibonacci(n):
    a, b = 1, 1
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

n = int(input("Enter terms: "))
fibonacci(n)
