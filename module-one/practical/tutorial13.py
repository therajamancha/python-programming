# class and object ( object oriented programming )

# creating and an object

class Rectangle:
    def __init__(self, length, breadth):  # constructor of the class
        # class attribute
        self.length = length
        self.breadth = breadth
        # medthod

    def calculate_area(self):
        return self.length * self.breadth


# creating instence with class
react = Rectangle(10, 5)
print("length", react.length, "breadth", react.breadth)
print("area", react.calculate_area())


class Student:
    # class variable (all instance have same value )
    teacher = "Mr David"
    room = "10A"

    def __init__(self, name, age):
        # instance variable (all student haeve there uniqe name and age )
        self.name = name
        self.age = age


tom = Student("tom", 18)
print(tom.name, "teacher :", tom.teacher)
susain = Student("susain", 18)
susain.teacher = "Mrs Gina"
print(susain.name, "teacher :", susain.teacher)
