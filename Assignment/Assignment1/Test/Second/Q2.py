#   WAP to accept 3 digit number. if 1st digit is double of second digit and half of
#  third digit then display "Yes,you have done it",otherwise display,
# "Please try next time".

num = int(input("Enter three digit number :"))

third = num % 10
num = num // 10

second = num % 10
num = num // 10

first = num % 10
num = num // 10

if(first != 2 * second):
    print("please try next time")
else:
    if(first == third / 2):
        print("yes , you have done it")


