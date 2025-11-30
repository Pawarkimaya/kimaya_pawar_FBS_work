#12. Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter any three digit number :"))
final_number = 0


remaining_amt = num // 10
firstdigit = num % 10
seconddigit = remaining_amt % 10
thirddigit = remaining_amt // 10

final_number = firstdigit * 100 + seconddigit * 10 + thirddigit * 1
print(final_number,firstdigit,seconddigit,thirddigit)
if(final_number == num):
    print("Given number is palindrome number.")
else:
    print("not palindrome number.")




