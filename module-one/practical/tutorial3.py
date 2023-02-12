from random import randint
name = input( "Enter you name : " ) 
age = input ( "Enter your age : " )
user_id = randint(100,999)
list1 = [user_id, name, age]
print (list1)

list2 = ["surat","gujrat",[2000,2001],23]

print (list2[0])

print (list2[-1])

print (list2[-2][0])

print (list2[0:3])

new_list = list2 + [24,25] 
print (new_list)

print ('surat' in list2)

new_list[-1] = "age"
print (new_list)

list2.extend(["india"])
print(list2)

list1.append(0)
print (list1)

list2.remove("india")
print (list2)

del list2[3]

print (list2)

del list2 [0 : 2]

print(list2)

list2.pop()

print(list2)

L = [32,48,65,92,45,56]

print(L.sort())
print(L)

print(L.sort(reverse=True))

print(L)

L = ["banana","apple","kivi"]

b = sorted(L)
print(b)

print(L)

word = ['1','2','3','4']
word[ : ] = [ ] 
print(word)

a =  ["banana","apple","kivi"]
b = a[:]
print (a,b)

a [0] = "strowbarry"
print (a,b)