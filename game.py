class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
    
    def area(self):
        return self.side ** 2

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)
square = Square(4)
print(f"The area of the circle is: {circle.area()}")       
print(f"The area of the rectangle is: {rectangle.area()}") 
print(f"The area of the triangle is: {triangle.area()}")   
print(f"The area of the square is: {square.area()}")

'''
The area of the circle is: 78.53975
The area of the rectangle is: 24
The area of the triangle is: 10.5
The area of the square is: 16
'''