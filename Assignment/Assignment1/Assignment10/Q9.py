# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

li = [1, 2, 2, 3, 4, 4, 5]

li2 = li.copy()

li.append(100)
print(li)
print(li2)

