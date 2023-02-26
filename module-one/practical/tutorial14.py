# method (static, class, instance )

class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
    # instance method

    def area(self):
        return Circle.PI * (self.radius ** 2)

    # class method (can not access radius)
    @classmethod
    def access_pi(cls): #have to give this parms 
        PI = 3.1436
        return PI

    # static methos ( can not access PI and redius )
    @staticmethod
    def static_method():
        return "this is static method"


cir = Circle(5)

print("circle radius :", cir.area())

print("class methos :", cir.access_pi())

print("static method :", cir.static_method())
