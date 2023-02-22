# function

number = int(input("Enter a number to get factorial : "))


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


print(factorial(number))

# function paremeter

# default peremeter


def greeting(name, msg="Welcome !"):
    print(name, msg)


greeting("Raj", "How are you?")
greeting("Jhone")

# args


def sum_number(*args):
    print(args)
    print(type(args))  # tuple
    sum = 0
    for n in args:
        sum += n
    return sum


print(sum_number(12, 3))


def func(x, y=1):
    z = x * y + x + y
    return z


print(func(2, func(3)))

# lambda function


def f(x): return "even" if x % 2 == 0 else "odd"


print(f(2))

greater = lambda x,y : x if x > y else y
print(greater(4,5))