class Student:
    def __init__(self, name, roll_no, marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Student Details")
        print(f"Name:- {self.name}")
        print(f"Roll No:- {self.roll_no}")
        print(f"Marks:- {self.marks}")


s1=Student("Srikanta", "23B81A05KM", 98)
s2=Student("Vrushank", "23B81A05Kv", 96)

s1.display()
s2.display()