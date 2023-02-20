# set ( uniqe sequences of data )
# creating set
list_1 = [1, 3, 2, 4, 4]
set_1 = set(list_1)
print(set_1)  # create an order data with uniqe value in it

# length
print(len(set_1))

# type
print(type(set_1))

# mutable
a = {1, 2, 3, 4}

a.add("india")
print(a)

a.remove("india")
print(a)

# set operation
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# union
print(A | B)
print(A.union(B))

# intersection
print(A & B)
print(A.intersection(B))

# difference
print(A - B)
print(A.difference(B))

# symetric deffrence
print(A ^ B)
