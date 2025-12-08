num = int(input("Enter number : "))
temp = num

#count total no. of digits
count = 0
while(temp > 0):
    temp = temp // 10
    count += 1
# print(count)

#calculate sum and power
temp = num 
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    mult = 1

    #calculate power
    for i in range(count):
        mult = mult * d
    # print(mult)

    #calculate sum
    sum = sum + mult
# print(sum)

#to check it is armstrong or not
if(sum == num):
    print(f'{num} is an armstrong number .')
else:
    print(f'{num} is not an armstrong number .')
