#    1
#   1 1
#  1 2 1
# 1 3 3 1

from math import factorial

rows = 4

for i in range(rows):          # i = row number
    for space in range(rows-i-1):
        print(" ", end="")

    for r in range(i+1):       # r = column number
        ncr = factorial(i) // (factorial(r) * factorial(i-r))
        print(ncr, end=" ")

    print()
