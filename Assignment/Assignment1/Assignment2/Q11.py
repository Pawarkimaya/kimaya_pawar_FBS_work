#WAP to accept an integer ammount and tell minimum number of notes needed

amount = int(input("Enter ammount :"))

n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10

minnote = n2000 + n500 + n200 + n100 + n50 + n20 + n10
print("Minimum numbers of notes :",minnote)







