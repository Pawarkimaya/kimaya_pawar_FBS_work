#6. WAP to check if a given number is prime number or not.
# Accept the number (n).
# If n ≤ 1 → it is NOT a prime number.
# Run a loop from 2 to (n // 2)
# For each number i in that range:
# If n % i == 0, then
# → n is NOT prime (because it has a divisor other than 1 and itself)
# → stop checking further.
# If the loop completes without finding any divisor:
# → n IS prime.

n = int(input("Enter number :"))
i = 1
for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is not prime number.")
        break
else:
    print(f"{n} is prime number.")