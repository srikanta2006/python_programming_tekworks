s_name=input("Enter the name of the student ")
s_number=int(input("Enter the number of the student "))
marks=map(int, input("Enter the marks of three subjects").split(" "))
total=sum(marks)
avg=total/3
#student report
print("STUDENT DETAILS")
print("Name:-", s_name)
print("Number:-", s_number)
print("Total_marks:-", total)
print("Average_marks:-", round(avg, 2))