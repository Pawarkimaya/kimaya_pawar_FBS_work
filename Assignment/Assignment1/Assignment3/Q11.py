'''Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

total_amt = 0

ticket = int(input("per person ticket ammount :"))

per1 = int(input("Please enter your first person age :"))

if(per1 < 12):
    first = ticket * 0.30
    print("First person amount",first,"Rs")
else:
    if(per1 > 59):
        first = ticket * 0.50
        print("First person amount",first,"Rs")
    else:
        first = ticket 
        print("First person amount",first,"Rs")

per2 = int(input("Please enter your age :"))

if(per2 < 12):
    second = ticket * 0.30
    print("2nd person amount",second,"Rs")
else:
    if(per2 > 59):
        second = ticket * 0.50
        print("2nd person amount",second,"Rs")
    else:
        second = ticket 
        print("2nd person amount",second,"Rs")

per3 = int(input("Please enter your age :"))

if(per3 < 12):
    third = ticket * 0.30
    print("3rd person amount",third,"Rs")
else:
    if(per3 > 59):
        third = ticket * 0.50
        print("3rd person amount",third,"Rs")
    else:
        third = ticket 
        print("3rd person amount",third,"Rs")

per4 = int(input("Please enter your age :"))
if(per4 < 12):
    fourth = ticket * 0.30
    print("4th person amount",fourth,"Rs")
else:
    if(per4 > 59):
        fourth = ticket * 0.50
        print("4th person amount",fourth,"Rs")
    else:
        fourth = ticket 
        print("4th person amount",fourth,"Rs")

per5 = int(input("Please enter your age :"))
if(per5 < 12):
    fifth = ticket * 0.30
    print("5th person amount",fifth,"Rs")
else:
    if(per5 > 59):
        fifth = ticket * 0.50
        print("5th person amount",fifth,"Rs")
    else:
        fifth = ticket 
        print("5th person amount",fifth,"Rs")
    
    total_amt = first + second + third + fourth + fifth

    print("Total ammount required for five person is :",total_amt)

