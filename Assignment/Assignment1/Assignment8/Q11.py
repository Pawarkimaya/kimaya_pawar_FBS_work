def is_armstrong(num):
    temp = num
    s = 0
    digits = len(str(num))

    while temp > 0:
        s = s + (temp % 10) ** digits
        temp = temp // 10

    if s == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


num = int(input("Enter number: "))
is_armstrong(num)
