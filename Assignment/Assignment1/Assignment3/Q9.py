#Input 5 subject marks from user and display grade(eg.First class,Second class ..)\

s1=(int(input("Enter mark of Marathi: ")))
s2=(int(input("Enter mark of English: ")))
s3=(int(input("Enter mark of Maths: ")))
s4=(int(input("Enter mark of Hindi: ")))
s5=(int(input("Enter mark of History: ")))

#calculate total marks
total=s1 + s2 + s3 + s4 +s5
#calculate percentage
percentage=(total/500)*100
if(percentage < 35):
    print("Failed.")
else:
    if percentage < 50:
        print("Pass class.")
    else:
        if percentage < 60:
            print("Second class.")
        else:
            if percentage < 75:
                print("First class.")
            else:
                print("You are pass with Distinction.")

