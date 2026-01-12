
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(i, i+i-1):
        print(j, end=" ")
    for j in range(i+i-3, i-1, -1):
        print(j, end=" ")
    print()
