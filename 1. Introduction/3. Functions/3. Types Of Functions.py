####################################################################--------------------IN BUILT FUNCTIONS----------------------------
#----------------------------------------------------
#1. abs()
num1 = -500
print("abs(num1):", abs(num1))
#abs() will always return positive number
#----------------------------------------------------
#2. all()
l1 = [5,4,3,2,1]
print("all(l1):", all(l1))

l2 = [1, 3, 4, 5, 0]
print("all(l2):", all(l2)) # because 0 is present

l3 = [] #empty list will always return true
print("all(l3):", all(l3))

l4 = [ 2,4,False ] #False in a list
print("all(l4):", all(l4))
#----------------------------------------------------
#3. dir() 
#return list of valid attributes
l5 = [1,2,4,5]
print("dir(l5):",dir(l5))
#----------------------------------------------------
#4. divmod()
result = divmod(10,2)
print("divmod(10,2): ", result, "-> Quotient: {} and Remainder: {}".format(result[0],result[1]))
#----------------------------------------------------
#5. enumerate()
l6 = [10,20,30,40,50]

for index, num in enumerate(l6): #by default index is 0
  print("index {} has value {}".format(index,num))

for index, num in enumerate(l6,101): 
  print("index {} has value {}".format(index,num))
#----------------------------------------------------
#6. filter()
def positiveNum(num):
  """
  Given function returns positive number
  """
  if num > 0:
    return num

l7 = range(-5,6)
print(list(l7))

positive_Numbers = list(filter(positiveNum, l7))
print(positive_Numbers)
#----------------------------------------------------
#7. isinstance()
l8 = [1,2,3,4,5,6]
print("isinstance(l8):", isinstance(l8,list))
print("isinstance(l8):", isinstance(l8,tuple))
print("isinstance(l8):", isinstance(l8,set))
print("isinstance(l8):", isinstance(l8,dict))
#----------------------------------------------------
#8. map()
l9 = [1,2,3,4,5]

def cubes(num):
  """
  Function returns cube of a number
  """
  return num ** 3

cubes = list(map(cubes,l9))
print("CUBES:", cubes)
#----------------------------------------------------
#9. reduce()
from functools import reduce

l10 = [ 1,2,3,4,5]
def product(num1, num2):
  """
  Function returns product of TWO Numbers
  """
  return num1*num2

result2 = reduce(product,l10)
print(result2)
#----------------------------------------------------
###################################################################


####################################################################------------------- USER DEFINED FUNCTIONS -----------------------
def product(num1, num2):
  """
  User Defined Function to find Product of TWO Numbers
  """
  return num1 * num2

print("Product = ", product(11,11))
###################################################################
