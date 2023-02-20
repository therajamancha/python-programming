# relational oprator
print(1 == 0)
print(1 != 0)
print(1 > 0)
print(1 >= 0)
print(1 < 0)
print(1 <= 0)

# dicion operator
a = 23
if a >= 18:
    print(a, "is grater then 18")
else:
    print(a, "is leser then 18")

# dicion making with user input
age = int(input("Enter your age : "))

if age >= 18 and age <= 60:
    print("You can vote")
else:
    print("You can not vote")

input_str = input()

if (input_str.startswith('analytics')):
    print("YES")
else: 
    print("NO")

