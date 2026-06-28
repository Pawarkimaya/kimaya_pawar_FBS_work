# 3. Write a program to find the second 
# largest element in the list.
li = [1,20,30,40,50,60,70,80,90]

def smax_ele(li):
    maximum = li[0]
    smax = li[0]

    for i in li:
        if i > maximum:
            smax = maximum
            maximum = i
        elif i > smax :
            smax = i

    return smax

smax_ele(li)
print(f'Second maximun element in list is {smax_ele(li)}')