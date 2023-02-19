from random import randint
# list and its method
name = input("Enter you name : ")
age = input("Enter your age : ")
user_id = randint(100, 999)
list1 = [user_id, name, age]
print(list1)
# mested list
list2 = ["surat", "gujrat", [2000, 2001], 23]
# accesing list
print(list2[0])
# negetive indexing
print(list2[-1])

print(list2[-2][0])
# slicing
print(list2[0:3])
# list concatination
new_list = list2 + [24, 25]
print(new_list)
# membership (checking value is in this list)
print('surat' in list2)
# mutable means changeble 
new_list[-1] = "age"
print(new_list)
# concating or adding existing list
list2.extend(["india"])
print(list2)

list1.append(0)
print(list1)

list2.remove("india")
print(list2)

del list2[3]

print(list2)

del list2[0: 2]

print(list2)

list2.pop()

print(list2)

# sort existing list
L = [32, 48, 65, 92, 45, 56]

print(L.sort())
print(L)

print(L.sort(reverse=True))

print(L)

# sorted create new sorted list
L = ["banana", "apple", "kivi"]

b = sorted(L)
print(b)

print(L)

word = ['1', '2', '3', '4']
word[:] = []
print(word)

# shadow coping (A = B) if you change a b automaticlly change
a = ["banana", "apple", "kivi"]
b = a[:]
print(a, b)

a[0] = "strowbarry"
print(a, b)
