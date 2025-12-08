# 11. WAP to check if given number Strong Number.
# Input a number

# Split it digit by digit

# For each digit → find factorial

# Add all factorials

# Compare sum with original number

# If equal → Strong number
# Else → Not a strong number

num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10

    # find factorial of this digit
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    num = num // 10

if sum == original:
    print(original, "is a Strong Number")
else:
    print(original, "is NOT a Strong Number")
