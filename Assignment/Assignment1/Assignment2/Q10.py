#WAP to reverse three digit number

num = int(input("Enter three digit number :"))

d1 = num % 10

d2 = (num//10)%10

d3 = num // 100

reverse = (d1 * 100) + (d2 * 10) + (d3 * 1)

print ("final result is :",reverse)

