# 2. Write a program to find maximum and minimum element in a list.

li = [1,20,30,40,50,60,70,80,90]

def max_ele(li):
    maximum = li[0]

    for i in li:
        if i > maximum:
            maximum = i
        
    return maximum

max_ele(li)
print(f'Maximun element in list is {max_ele(li)}')


def min_ele(li):
    minimum = li[0]

    for i in li:
        if i < minimum:
            minimum = i
        
    return minimum



min_ele(li)
print(f'Minimum element in list is {min_ele(li)}')




