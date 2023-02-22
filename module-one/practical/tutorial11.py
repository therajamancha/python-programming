# map filter reducer method
from functools import reduce
# create list of uppercase countries
countries = ["India", "Japan", "Italy", "France"]


def f(x): return x.upper()


method_one = []
for country in countries:
    method_one.append(f(country))

print(method_one)

method_two = [f(country) for country in countries]

print(method_two)

# map method
# first is function or lamda function  and second itrable list
method_three = list(map(f, countries))

print(method_three)

# filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def div_by(x): return x % 3 == 0


div_list = list(filter(div_by, numbers))

print(div_list)

students = {1: ["Raj", 23], 2: ["Kishan", 22], 3: ["monik", 17]}

check_age = lambda x: x[1] >= 18

old_students = list(filter(check_age,students.values()))

print(old_students)

list_of_no = [2,4,6]

total = lambda x,y : x + y

add_numbers = reduce(total,list_of_no)

print(add_numbers)

