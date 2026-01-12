def is_palindrome(num):
    temp = num
    rev = 0

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp = temp // 10

    if num == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")


num = int(input("Enter number: "))
is_palindrome(num)
