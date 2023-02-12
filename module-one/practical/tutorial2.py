name = 'Raj'
char = "A"
print(name, char)

print( "I don't cheat")

print ( 'I don\'t cheat' )

flavour = input ("Enter a flavour : ")
desert_type = input ("Enter you deser type : ")
print ( "You have enterd, ", flavour+ " "+desert_type )

fname = input ("enter first name ")
lname = input ( "enter last name " )

full_name = fname+" "+lname
print(full_name)

string = "My name is Raj and I am bca student at upgarde"
print(len(string))

print(string[0])

print(string[-1])

print(string[len(string) - 1])

students = "5 girls and 3 boys"
girls = students[:7]
boys = students[11:]
print (girls , boys)

quote = "this is quote"
print ("this" in quote)

upper_txt = "this is uppercase"
print(upper_txt.upper())

lower_txt = "THIS IS LOWERCASE"
print (lower_txt.lower())

end_trim = "thi is end trim   "
print ( end_trim.rstrip() )

start_trim = "   this is start trim"
print (start_trim.lstrip())

str_txt = "this is sample text"
print (str_txt.count('i'))

print (str_txt.count('i',5))

a = "Data"
b = "analys"
c = "Pandas"
print (a, b, "using", c)

print ( "{0} {1} using {2}".format(a,b,c))