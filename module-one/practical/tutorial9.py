# Comprehensions

brand = ["HoNda", "bENZ", "KiA", "ToyotA", "RenaUlt"]

length_of_brand = []
for word in brand:
    length_of_brand.append(len(word))

print(length_of_brand)

# Comprehensions way
capitalize_brand = [word.capitalize() for word in brand]

print(capitalize_brand)

# itration in simulation

for word, length in zip(capitalize_brand, length_of_brand):
    print(word, ":", length)

# dictionary in comprehensions

car_length = {word: len(word) for word in capitalize_brand}
print(car_length)

name = input("Enter your name : ")
vowels_in_name = set()
for char in name:
    if char in "aeiouAEIOU":
        vowels_in_name.add(char)

print(vowels_in_name)

# comp Way
vowels = {char for char in name if char in "aeiouAEIOU"}
print(vowels)
