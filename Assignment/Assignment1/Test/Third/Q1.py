##WAP to print first n prime numbers.

n = int(input("Enter number: "))
count = 0

print("First prime numbers are: ")

num = 2

while count < n :
    for i in range(2,num):
        if num % i == 0 :
            break
    else:
            print(num)
            count+=1
    num+=1
      
    