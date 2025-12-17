# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total = 0

num = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost: "))

for i in range(num):
    age = int(input(f"Enter age of passenger {i+1}: "))

    if age < 12:
        amount = cost * 0.70   # 30% discount
    elif age > 59:
        amount = cost * 0.50   # 50% discount
    else:
        amount = cost          # full cost

    total += amount

print("Total amount to pay =", total)
