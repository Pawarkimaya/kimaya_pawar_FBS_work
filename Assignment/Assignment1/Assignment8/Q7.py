def sum_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s

num = int(input("Enter number: "))
print(sum_digits(num))
