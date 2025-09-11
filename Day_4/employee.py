class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Student Details")
        print(f"Name:- {self.name}")
        print(f"Salary:- {self.salary}")

class Manager(Employee):
    def __init__(self,name , salary, department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        super().display()
        print(f"Department:- {self.department}") 

s1=Employee("Srikanta", 2000000)
s2=Manager("Vrushank", 1000000,"R&D")

s1.display()
s2.display()