#WAP to check if the number given is positive , negative or neutral
num = int(input("Enter number :"))
if(num == 0):
    print(f'{num} is a neutral number.')
elif(num>0):
    print(f'{num} is a positive number.')   
else:
    print(f'{num} is a negative number.')

    print("End of Program")