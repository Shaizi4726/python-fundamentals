import math


class Shape:
    def __init__(self, color, shape_type=None):
        self.color = color
        self.shape_type = shape_type

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def __str__(self):
        return f"Type: {self.shape_type}, Color: {self.color}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    shape_type = "Circle"

    def __init__(self, color, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        super().__init__(color, self.shape_type)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    shape_type = "Rectangle"

    def __init__(self, color, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be greater than 0.")
        super().__init__(color, self.shape_type)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    shape_type = "Triangle"

    def __init__(self, color, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be greater than 0.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(
                "Invalid triangle — sides violate triangle inequality.")
        super().__init__(color, self.shape_type)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        triangle_area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return triangle_area

    def perimeter(self):
        return self.a + self.b + self.c


class Square(Rectangle):
    shape_type = "Square"

    def __init__(self, color, side):
        super().__init__(color, side, side)


def main():
    try:
        circle = Circle("Red", 10)
        print(circle)
    except ValueError as e:
        print(e)

    try:
        rectangle = Rectangle("Green", 20, 10)
        print(rectangle)
    except ValueError as e:
        print(e)

    try:
        triangle = Triangle("Yellow", 11, 13, 20)
        print(triangle)
    except ValueError as e:
        print(e)

    try:
        square = Square("Blue", -2)
        print(square)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
