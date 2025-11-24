#WAP  to enter P,T,R and calculate simple intrest 
P=(float(input("Enter Principle ammount:",)))
T=(float(input("Enter time in years:")))
R=(float(input("Enter rate of intrest:")))

#apply formula
SI=(P*T*R)/100

print("Simple intrest of given ammount is:",SI,"%")
