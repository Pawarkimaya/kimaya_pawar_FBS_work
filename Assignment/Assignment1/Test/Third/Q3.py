##WAP to accept basic salary of n employee (n should be accepted from user)
n=int(input("Enter n number of employee: "))
grand_total=0
for i in range(1,n+1):
    basic_sal=int(input(f'Enter basic salary of employees {i} : '))
    
    if basic_sal < 20000 :
        da = basic_sal * 0.10
        ta = basic_sal * 0.12
        hra = basic_sal * 0.15
    else:
        da = basic_sal * 0.15
        ta = basic_sal  * 0.18
        hra = basic_sal * 0.20
        
    total = basic_sal + da +ta +hra
    grand_total+=total
        
    print(f'Total salary of employee is {total}')

print("Total salary of all employee = ",grand_total)


