1. #WAP to print all even numbers until n.

n = int(input("Enter number :"))

#for i in range(0,n+1, 2):
 #   print(i)

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
