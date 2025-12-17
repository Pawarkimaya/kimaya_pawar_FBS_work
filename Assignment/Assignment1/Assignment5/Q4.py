# 4. WAP to print Armstrong number within a given range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    temp = num
    count = 0

    
    while temp > 0:
        temp = temp // 10
        count += 1

    temp = num
    sum_powers = 0

    while temp > 0:
        digit = temp % 10
        sum_powers += digit ** count
        temp = temp // 10


    if sum_powers == num:
        print(num)
