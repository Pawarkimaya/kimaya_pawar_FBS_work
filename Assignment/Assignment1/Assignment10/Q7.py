# 6. Write a program to remove duplicates from the list.
a = [1, 2, 2, 3, 4, 4, 5]
u = []

for x in a:
    if x not in u:
        u.append(x)
print(u)