#WAP to convert days into years,weeks and days
days = (int(input("Please enter days:")))

#calculate years
year = days // 365
#remaining days
remaining_days = days % 365

#calculate weeks
weeks = remaining_days // 7

#calculate days
days_left = remaining_days % 7

#print
print("Year :",year)
print("Weeks :",weeks)
print("Days :",days_left)
