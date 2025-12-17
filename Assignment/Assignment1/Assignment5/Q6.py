n = int(input("How many prime numbers? "))

count_primes = 0   
num = 2            

while count_primes < n:
    count = 0      

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:    
        print(num)
        count_primes += 1

    num += 1
