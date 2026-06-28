# # 1. Write a program to find sum of all elements of list

li = list(map(int, input("Enter numbers separated by space: ").split()))

sum = 0

for i in li:
    sum = sum + i

print(sum)

print("List:", li)

li2 = list(map(int, input("Enter numbers separated by space : ").split()))