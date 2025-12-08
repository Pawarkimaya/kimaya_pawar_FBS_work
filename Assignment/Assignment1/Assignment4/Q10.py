# 10. WAP to check if given number is Perfect Number.

num = int(input("Enter number: "))
sum = 0 
for i in range(1, num):
    if num % i == 0:
        sum =sum +i
    else:
        continue
    
if(num == sum):
        print(f"{num} is perfect number.")
else:
    print(f"{num} is not a perfect number.")