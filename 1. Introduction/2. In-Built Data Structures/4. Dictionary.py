### Dictionary Creation
print("DICTIONARY CREATION:")
#Empty Dictionary
d1 = {}
print(type(d1))

d2 = {'Name': 'Chanakya', 'Address': 'Patliputra'}
print(d2)

d3 = {1: 'One', 2: 'Two', 3: 'Three'}
print(d3)

d4 = {'Name': 'Chanakya', 101: ['Neeti', 'Arthashastra']}
print(d4 ,"\n")
#------------------------------------------------------------------

### Dictionary Access
print('DICTIONARY ACCESS:')
d5 = {'Name': 'Chanakya', 101: ['Neeti', 'Arthashastra']}
print(d5['Name'])

#Below command will give key error -as 'any' key is not present
# print(d5['any']) 
#while this will not give an error
print(d5.get('any'))

#another way of accessing key
print(d5.get(101), "\n")
#------------------------------------------------------------------

### Dictionary Add And Modify
print("ADD AND MODIFY:")

d6 = {'Name': 'Chanakya', 101: ['Neeti', 'Arthashastra']}

#update Name
d6['Name'] = 'Chandragupta';
print(d6)
#Add new key
d6['King Of'] = ['magdha', 'patliputra']
print(d6, "\n")
#------------------------------------------------------------------

### Dictionary Delete Or Remove Element
print("DELETE ELEMENT:")

d7 = {'Name':    'Chandragupta', 101: ['Neeti', 'Arthashastra'],
      'King Of': ['magdha', 'patliputra']}
print(d7.pop(101))
print(d7)

#remove an arbitarty key
print(d7.popitem())
print(d7)

#delete whole dictionary
d8 = {1: 'One', 2: 'Two', 3: 'Three'}
del d8
#this will give error
# print(d8)

#Delete Particular key
d9 = {1: 'One', 2: 'Two', 3: 'Three'}
del d9[1]
print(d9)

#remove all elements
d9.clear()
print(d9, "\n")
#------------------------------------------------------------------

### Dictionary Methods
print("DICTIONARY METHODS:")

d10 = {1: 'One', 2: 'Two', 3: 'Three'}
d10dup = d10.copy()
print(d10dup)

#fromkeys[seq[, v]] -> Return a new dictionary with keys from seq and value equal to v (defaults to None).
d11 = {}.fromkeys(['First', 'Second', 'Third'], 202)
print(d11)

#return a new view of the dictionary items (key, value)
print(d10.items())
#return Keys
print(d10.keys())
#return Values
print(d10.values())

#get list of all available methods and attributes of dictionary
d = {}
print(dir(d), "\n")
#------------------------------------------------------------------

### Dictionary Comprehension
print('DICTIONARY COMPRENHENSION:')
d12 = {1: 'One', 2: 'Two', 3: 'Three'}
for pair in d12.items():
  print(pair)

#Creating a new dictionary with only pairs where the value is larger than 5
d13 = {'x1': 1, 'x2': 2, 'x3': 3, 'x4': 4}
d14 = {k:v for k, v in d13.items() if v <= 3}
print(d14)

#operations on the key value pairs
d15 = {'x1': 1, 'x2': 2, 'x3': 3, 'x4': 4}
d15 = { k + '0': v*10 for k,v in d15.items() if v<=3}
print(d15)
#------------------------------------------------------------------