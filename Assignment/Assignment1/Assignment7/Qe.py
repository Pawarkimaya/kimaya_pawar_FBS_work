n = 5
for i in range(1, n):
    for j in range(1, n+1):
        if j == 1 or j == i+1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, n+1):
    print(i, end=" ")
