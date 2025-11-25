#WAP to enter P,T,R and calculate Compound intrest 
P=(float(input("Enter Principle ammount:",)))
T=(float(input("Enter time in years:")))
R=(float(input("Enter rate of intrest:")))

#apply formula
A=P*(1+R/100)**T
CI=A-P

print("Compound intrest of given ammount is",CI,"%")
print("Ammount is",A)