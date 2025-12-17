# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
students = int(input("Enter number of students: "))

total_percentage = 0   

for s in range(1, students + 1):
    print("\nStudent", s)

  
    m1 = int(input("Enter marks for subject 1: "))
    m2 = int(input("Enter marks for subject 2: "))
    m3 = int(input("Enter marks for subject 3: "))
    m4 = int(input("Enter marks for subject 4: "))
    m5 = int(input("Enter marks for subject 5: "))

    total = m1 + m2 + m3 + m4 + m5         
    percentage = total / 5                  
    print("Percentage of student", s, "=", percentage)

    total_percentage += percentage          

average = total_percentage / students

print("\nAverage Percentage of all students =", average)



