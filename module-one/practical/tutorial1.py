print("Hello world")

name = input( "What's you name? " )

print ( "*" * 10 )

print( "welcome to upgrad",name )

# data type

var1 = "Raj" #string
print(var1)

var2 = 1 #number
print(var2)

var3 = 23.3 #floating
print(var3)

# get value from user and doing operation on it

age = input ("Enter your age:")
age = int(age) #converting string input to integer 
print( "you are " , age * 12 ,  "month old" )

# type casting in python

interger_num = 99
floating_num = 98.00
string = "Raj"
boolean = True

print(type(interger_num))

print(type(floating_num))

print(type(string))

print(type(boolean))


a = 1 # interger variable
print ( bool(a))

print (float(a))

print ( str(a))

a = 7
b = 6
print ( "addition ", a + b )

print ( "subtraction ", a - b )

print ( "multiplication ", a * b )

print ( "divistion ", a / b )

print ( " floor divistion ", a // b )

print ( ( 4 * 5) - 9 + 6 / 7 )

4 % (1 + 9)**2 - 60 // (7 + 2)