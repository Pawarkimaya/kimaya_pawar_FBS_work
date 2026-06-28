# 6. Write a program to remove duplicates from the list.li = [10,20,30,40,50,60,70,80,90,10]

li = [10,20,30,40,50,60,70,80,90,10]

ele = int(input("Enter element : "))


def check(li, ele):
    count = 0

    for i in li:
        if i == ele:
            count += 1

    if count > 1:
        print("Present")
        li.remove(i)
        print("Count =", count)
    else:
        print("Not Present")

check(li, ele)

