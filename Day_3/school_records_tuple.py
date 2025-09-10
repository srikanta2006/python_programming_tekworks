def highest_marks(my_list):
    max_marks=0
    student=""
    for item in my_list:
        if(item[2]>max_marks):
            max_marks=item[2]
            student=item[0]
    return student

def more_than_75_marks(my_list):
    students=[]
    for item in my_list:
        if(item[2]>75):
            students.append(item[0])
    print(students)

def make_list():
    for i in range(5):
        name=input("Enter the name of student")
        roll_no=input("Enter the roll number of student")
        marks=int(input("Enter the marks of student"))
        my_list.append((name, roll_no, marks))
my_list=[]
make_list()
print(highest_marks(my_list))
