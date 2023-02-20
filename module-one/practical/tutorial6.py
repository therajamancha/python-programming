# dictionary
# creating
d = {"India": "INR", "USA": "USD", "France": "Euro"}

# printing
print(d["India"], d["USA"])

# updating
d["USA"] = "$"
print(d)

# insert new key value pair
d["Japan"] = "Yen"
print(d)

# delete key value
del d["France"]
print(d)

# sorted
print(sorted(d))

# get all values
print(d.values())
# get all keys
print(d.keys())

# update method
d.update({"USA": "USD"})
print(d)

input_dict = {'Jack Dorsey': 'Twitter', 'Tim Cook': 'Apple',
              'Jeff Bezos': 'Amazon', 'Mukesh Ambani': 'RJIO'}
print(sorted(input_dict.values()))