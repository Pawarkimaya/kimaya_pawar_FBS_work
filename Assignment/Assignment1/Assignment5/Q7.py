# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

print("Choose a series:")
print("1. 1! + 2! + 3! + ... + n!")
print("2. N + N^2 + N^3 + ... + N^N")
print("3. Geometric series (1 + 2 + 4 + ... upto n)")
print("4. S = a + a^2/2 + a^3/3 + ... + a^10/10")
print("5. x - x^2/3 + x^3/5 - x^4/7 ... upto n terms")

choice = int(input("Enter choice (1-5): "))


# ------------------ SERIES A ------------------
if choice == 1:
    n = int(input("Enter n: "))
    total = 0

    for num in range(1, n+1):
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
        total = total + fact

    print("Sum =", total)


# ------------------ SERIES B ------------------
elif choice == 2:
    N = int(input("Enter N: "))
    total = 0

    for p in range(1, N+1):
        total = total + (N ** p)

    print("Sum =", total)


# ------------------ SERIES C ------------------
elif choice == 3:
    n = int(input("Enter n: "))
    term = 1
    total = 0

    for i in range(1, n+1):
        total = total + term
        term = term * 2

    print("Sum =", total)


# ------------------ SERIES D ------------------
elif choice == 4:
    a = int(input("Enter a: "))
    total = 0

    for p in range(1, 11):
        total = total + (a ** p) / p

    print("Sum =", total)


# ------------------ SERIES E ------------------
elif choice == 5:
    x = int(input("Enter x: "))
    n = int(input("Enter number of terms: "))

    total = 0
    power = 1
    den = 1
    sign = 1

    for i in range(1, n+1):
        term = (x ** power) / den
        total = total + (sign * term)

        power += 1
        den += 2
        sign = sign * -1

    print("Sum =", total)


else:
    print("Invalid choice")
