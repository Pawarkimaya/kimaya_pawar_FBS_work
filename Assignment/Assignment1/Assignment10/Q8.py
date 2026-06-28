# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

a = [1, 2, 2, 3, 4, 4, 5]

u = []

for x in a:
    u.append(x * x * x)

print(u)