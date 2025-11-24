#WAP to calculate percentage of student based on marks of any 5 subject

#taking marks of 5 subject from user 

m1=(int(input("Enter mark of Marathi: ")))
m2=(int(input("Enter mark of English: ")))
m3=(int(input("Enter mark of Maths: ")))
m4=(int(input("Enter mark of Hindi: ")))
m5=(int(input("Enter mark of History: ")))
m6=(int(input("Enter mark of Geography: ")))
m7=(int(input("Enter mark of Science : ")))

#calculate total marks
total=m1+m2+m3+m4+m5+m6+m7
#calculate percentage
percentage=(total/560)*100
#print result
print("percentage=",percentage,"%")






