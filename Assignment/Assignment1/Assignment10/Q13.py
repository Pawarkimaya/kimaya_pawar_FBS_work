# 13 . Write a program to print list after removing even numbers.

li = [ 2,3,4,5,6,7,8,9,10 ]

print(li)


def remove(li):
    new = []
    
    for i in li:
        if i % 2 != 0:
            new.append(i)

    print(new)


remove(li)
