import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        print("Circle constructor")
    def area(self):
        print("Circle area",end=" =")
        return math.pi * self.radius ** 2
    def perimeter(self):
        print("Circle perimeter",end=" =")
        return 2 * math.pi * self.radius
circle1 = Circle(3)
print(circle1.area())
print(circle1.perimeter())