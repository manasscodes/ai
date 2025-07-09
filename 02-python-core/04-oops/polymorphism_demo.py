# Polymorphism using method overriding
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

for shape in [Shape(), Circle(), Square()]:
    shape.draw()