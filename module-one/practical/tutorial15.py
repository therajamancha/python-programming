# inheritence and overriding in python

class shap:

    def set_color(self, color):
        self.color = color

    def calculate(self):
        pass

    def color_the_shape(self):
        color_price = {"red": 10, "blue": 15, "green": 5}
        return self.calculate() * color_price[self.color]


class Circle(shap):  # inheritance
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # overriding
    def calculate(self):
        return Circle.pi * (self.radius ** 2)


c = Circle(5)

c.set_color("red")

print(c.radius, c.color)

print(c.color_the_shape())


class Rectangle(shap):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # override
    def calculate(self):
        return self.breadth * self.length

    # override python default method
    def __str__(self):
        return "area of rectangle =" + str(self.calculate())


r = Rectangle(5, 10)

r.set_color("blue")

print(r.length, r.breadth, r.color)

print(r.color_the_shape())

print(r)
