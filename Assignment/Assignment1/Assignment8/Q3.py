def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


# Function to find factorial
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


# Function for sum: 1! + 2! + 3! + ... + n!
def sum_factorial(n):
    s = 0
    for i in range(1, n+1):
        s = s + factorial(i)
    return s


# Function for sum: 1^1 + 2^2 + 3^3 + ... + n^n
def power_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + (i ** i)
    return s


# -------- MENU --------
while True:
    print("\nMENU")
    print("1. Sum of series: 1 + 2 + 3 + ... + n")
    print("2. Sum of series: 1! + 2! + 3! + ... + n!")
    print("3. Sum of series: 1^1 + 2^2 + 3^3 + ... + n^n")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter n: "))
        print("Sum =", sum_n(n))

    elif choice == 2:
        n = int(input("Enter n: "))
        print("Sum =", sum_factorial(n))

    elif choice == 3:
        n = int(input("Enter n: "))
        print("Sum =", power_sum(n))

    elif choice == 4:
        print("Program End")
        break

    else:
        print("Invalid choice")
