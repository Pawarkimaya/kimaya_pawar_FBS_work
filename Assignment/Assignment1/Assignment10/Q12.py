# 12. Write a program to create three lists 
# of numbers, 
# their 
# squares and 
# cubes

li = [1,2,3,4,5]

sq = []
cube = []

for i in li:
    sq.append(i*i)
    cube.append(i*i*i)

print(li)
print(sq)
print(cube)