from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return math.pi*(self.radius**2)
    

rec1=Rectangle(2,3)
cir1=Circle(3)

print(f"Area of rectangle:- {rec1.area()}")
print(f"Area of circle:- {round(cir1.area(), 2)}")