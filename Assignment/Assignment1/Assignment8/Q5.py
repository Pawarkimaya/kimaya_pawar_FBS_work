# 5. Sum of all prime numbers between 1 to n

def isprime(num):
    if num < 2:
        return "not prime"

    for i in range(2, num):
        if num % i == 0:
            return "not prime"
    return "prime"

def sumprime(n):
    total = 0
    for i in range(1, n+1):
        if isprime(i) == "prime":
            total += i
    return total


n = int(input("Enter number: "))
print("Sum of prime numbers:", sumprime(n))
