#2. WAP to print all odd numbers until n.

n = int(input("Enter number :"))

for i in range(n+1):
    if i % 2 != 0:
        print(i,end = " ")
    