# 10. Write a program to remove all occurrences 
# of a given element in the list.

li = [10,20,10,30,40,10]

ele = int(input("Enter which element you want to remove: "))

def remove(li, ele):
    new = []

    for i in li:
        if i != ele:
            new.append(i)

    return new

print(remove(li, ele))
