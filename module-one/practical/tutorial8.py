# loops and itration
# while loop example
import sys
pin = input("Enter a pin : ")
attempt_count = 1
while pin != "1234":
    if attempt_count >= 3:
        sys.exit("Too meny attempts")
    pin = input("Invalid pin Enter pin again : ")
    attempt_count += 1

print("Log in succesfully")

# for in loop
# itrate in list
list_one = [1, 2, 3, 4, 5, 6]
for element in list_one:
    print(element)

# itrate in string
print("\n")
country = "INDIA"
for char in country:
    print(char)

print("\n")
for char in country:
    print(char, end="")

# itrate in dictionary
obj = {
    "name": "Raj",
    "age": 23,
    "job": "web developer",
}

print("\n")
for key, val in obj.items():
    print(key, val)

for key in obj.keys():
    print(obj[key])

for i in range(1, 5):
    print(i, end="")

print(list(range(1, 100, 2)))

print(list(range(100, 1, -1)))
