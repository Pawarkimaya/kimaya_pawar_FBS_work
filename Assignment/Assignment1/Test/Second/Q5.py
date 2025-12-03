#A man goes for shopping.he buys 5 products.Accept the price of all product
# and display the total bill after adding 18% GST.

pro1 = int(input("Please enter price of 1st product :"))
pro2 = int(input("Please enter price of 2nd product :"))
pro3 = int(input("Please enter price of 3rd product :"))
pro4 = int(input("Please enter price of 4th product :"))
pro5 = int(input("Please enter price of 5th product :"))

gross_amt = pro1 + pro2 + pro3 + pro4 + pro5

GST = gross_amt * 18 / 100

net_amt = gross_amt + GST

print(f"Total bill before adding 18% of Gst is : {gross_amt}")

print(f"Total bill after adding 18% of GST is : {net_amt}")
