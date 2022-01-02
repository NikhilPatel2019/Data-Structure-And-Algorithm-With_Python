#Arithmetic Operators
#-----------------------------------------------------------------
x, y = 3, 2

#Addition
print('Addition: ', x+y)

#subtraction(-)
print('Subtraction', x-y)

#multiplication(*)
print('Multiplication', x*y)

#division(/)
print('Division', x/y)

#modulo division (%)
print('Remainder: ', x%y)

#Floor Division (//)
print('Flooe Division: ', x//y)

#Exponent (**)
print('Exponent: ', x**y)
#------------------------------------------------------------------

#Comparisons Operators
#------------------------------------------------------------------
a, b = 10, 20         

print(a < b)  #check a is less than b

#check a is greater than b
print(a > b)

#check a is equal to b
print(a == b)

#check a is not equal to b (!=)
print(a != b)

#check a greater than or equal to b
print(a >= b)

#check a less than or equal to b
print(a <= b)
#------------------------------------------------------------------

#Logical Operators
#------------------------------------------------------------------
t, f = True, False

#print t and f
print(t and f)

#print t or f
print(t or f)

#print true if t is not f
print( t is not f)
#------------------------------------------------------------------

#Bitwise Operators
#------------------------------------------------------------------
c, d = 10, 4

#Bitwise AND
print(c & d)

#Bitwise OR
print(c | d)

#Bitwise NOT
print(~ d)

#Bitwise XOR
print(c ^ d)

#Bitwise rightshift
print(c>>d)

#Bitwise Leftshift
print(c<<d)
#------------------------------------------------------------------

#Assignment Operators
#------------------------------------------------------------------
e = 10

e += 10         #add AND
print(e)

#subtract AND (-=)
e -= 10
print(e)

#Multiply AND (*=)
e *= 10
print(e)

#Divide AND (/=)
e /= 10
print(e)

#Modulus AND (%=)
e %= 3
print(e)

#Floor Division (//=)
e //= 2
print(e)

#Exponent AND (**=)
f = 2
f **= 3
print(f)
#------------------------------------------------------------------

#Special Opeartors
#------------------------------------------------------------------
#1. Identity Operators 
g = 5
h = 5
print(g is h)    #5 is object created once both a and b points to same object

#check is not
print(g is not h)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)

s1 = "Testing"
s2 = "Testing"
print(s1 is not s2)

#2. Membership Operators
lst = [1, 2, 3, 4]
print(1 in lst)       #check 1 is present in a given list or not

#check 5 is present in a given list
#------------------------------------------------------------------