# 4. Write a program to reverse the list.
# li = [10,20,30,40,50,60,70,80,90]

# def rev(li):
#     for i in range(len(li)-1,-1,-1):
#         print(li[i],end =" ")


# rev(li)

li = [10,20,30,40,50,60,70,80,90]

rev = []

for i in range(len(li)-1, -1, -1):
    rev.append(li[i])

print(rev)