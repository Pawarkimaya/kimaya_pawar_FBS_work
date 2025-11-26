#WAP to calculate selling price of book based on cost price and discount.

# selling price = (Cost price + discount)

cost=(int(input("Enter cost of the book:")))
discount=(int(input("Enter % discount you want apply :")))
dis=cost*discount/100

finalprice = cost - dis


print(f"Selling price of book is : {finalprice}")
