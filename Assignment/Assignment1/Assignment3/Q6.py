#Write a program to calculate profit or loss.
cp = int(input("Enter cost price of an item :"))
sp = int(input("Enter selling price of same item :"))

#profit
profit = sp - cp
perc = (profit/cp) * 100

#loss
loss = sp - cp
lass = (loss/cp) * 100

if(sp > cp):
    print("Congratulations..its a profit deal.")
    print("profit : ",perc,"%")
else:
    print("ohho...its an loss")
    print("loss : ",lass,"%")