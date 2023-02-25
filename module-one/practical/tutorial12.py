# practice map filter reduce
from functools import reduce

# Using the function Map, count the number of words that start with ‘S’ in input_list.


list_one = ['Santa Cruz', 'Santa fe', 'Mumbai', 'Delhi']


count = sum(map(lambda x: x[0] == 'S', list_one))
print(count)

# Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively.

first_name = ['Ankur', 'Avik', 'Kiran', 'Nitin']
last_name = ['Narang', 'Sarkar', 'R', 'Sareen']


def full_name(fname, lname):
    return fname + " " + lname


print(full_name("raj", "amancha"))

name = list(map(lambda f, n: f + " " + n, first_name, last_name))
print(name)

# Extract a list of numbers that are multiples of 5 from a list of integers named input_list.

list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

list_answer = list(filter(lambda a: 0 == a % 5, list_two))

print(list_answer)

# You are given a list of strings such as input_list = ['hdjk', 'salsap', 'sherpa'].Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.

input_three = ['soap', 'sharp', 'shy', 'silent', 'ship', 'summer', 'sheep']

sp = list(filter(lambda name: name.startswith(
    "s") and name.endswith("p"), input_three))

print(sp)

# Using the Reduce function, concatenate a list of words in input_list, and print the output as a string. If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.

input_four = ['All', 'you', 'have', 'to', 'fear', 'is', 'fear', 'itself']

print(reduce(lambda prev, nex: prev + " " + nex, input_four))

# You are given a list of numbers such as input_list = [31, 63, 76, 89]. Find and print the largest number in input_list using the reduce() function.

input_five = [65, 76, 87, 23, 12, 90, 99]

answer = reduce(lambda a, b: a if a > b else b, input_five)

print(answer)
