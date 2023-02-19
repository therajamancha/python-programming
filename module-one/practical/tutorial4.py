# tuple is imutable can not change tuple data
# we can do all method of list acapt mutation method
# define tuple
a = ("tuple", 12)
print(a)
print(type(a))

b = 1, 3, 4, 5, 6
print(b)

c = 1,
print(c)

# this is not tuple
d = 1
print(type(d))

e = (1)
print(type(e))

# indexing tuples
f = ("Raj", 23, "BCA")
print(f[0])
print(f[1])
print(f[-1])

# slicing tuple
g = "Raj", 23, "BCA", 4
print(g[:2])
print(g[-2:])

# lenght
print(len(g))

# conacting
tuple1 = 4, 5, 6
tuple2 = 1, 2, 3
tuple3 = tuple1 + tuple2
print(tuple3)

# sum min max (only work in integer tuple)
print("Sum", sum(tuple3))
print("Min", min(tuple3))
print("Max", max(tuple3))

# imutibilty in tupple
h = "Raj", 23, "BCA"
i = h[:1] + (24,) + h[2:]
print(i)

# sorting
j = sorted(tuple3)  # creating sorted list
k = tuple(j)  # typecasting into tuple
print(k)

# nested tuple
l = ("DSA", ("python", "java"))
print(l[1][1])

# unpacking
m = (1, 2, 3, 4, 5)
(n1, n2, n3, n4, n5) = m
print(n3)

# dir to wiew all method fot tuple
print(dir(m))