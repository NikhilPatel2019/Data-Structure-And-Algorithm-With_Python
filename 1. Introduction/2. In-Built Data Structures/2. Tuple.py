#Tuple cannot be changed(immutable)

#1. Tuple Creation
#empty tuple
tpl = ()

#tuple with integers
tp1 = (1,2,3,4,5)
print(tp1)

#tuple with mixed data type
tp2 = (1, 'kuch', 'bhi',2,4)
print(tp2)

#Nested Tuple
tp3 = (1,2,(3,4,5),[7,8,9], ['Ten','Eleven'],[12,13,'fourteen','fifteen', 16])
print(tp3) 

#Only parenthesis is not enough
tp4 = ('Testing')
print(type(tp4))

#need a comma at the end
tp5 = ('Testing',)
print(type(tp5))

#Parenthesis is optional
tp6 = "Testing",
print(type(tp6))
print("==========================================================")
#-----------------------------------------------------------------

#2. Accessing Elements
tp7 = ('One', 'Two', 'Three', 'Four')
print(tp7[2])
#negative index
print(tp7[-1])

#nested Tuple
tp8 = ('first',('second-a','second-b','second-c'))
print(tp8[1])
#printing nested tuple elements
print(tp8[1][0])
print(tp8[1][1])
print(tp8[1][2])

#slicing
tp9 = (1,2,3,4,5,6,7,8,9)
print(tp9[2:6])
print(tp9[:-3])
print(tp9[:])
print("==========================================================")
#-----------------------------------------------------------------

#3. Changing Elements
tp10 = (1,2,[3,4,5],6)
#tp10[1] = "Zero" #this will give an error
tp10[2][1] = "Changed"
print(tp10)

#tuple concatination
tp11 = (1,2,3,4,5) + (6,7,8,9,)
print(tp11)

#repeat the elements in a tuple for a given number of times using the * operator.
tp12 = (('Namaste',) * 5)
print(tp12)
print("==========================================================")
#------------------------------------------------------------------

#4. Tuple deletion
#we cannot change the elements in a tuple. 
# That also means we cannot delete or remove items from a tuple.

#delete entire tuple using del keyword
tp13 = (1, 2, 3, 4, 5, 6)

#delete entire tuple
del tp13
#------------------------------------------------------------------

#5. Tuple Count
tp14 = (1,2,2,2,3,3,4)
#get the frequency of particular element appears in a tuple
print(tp14.count(2))
#-----------------------------------------------------------------

#6. Tuple Index
#return index of the first element is equal to 3
print(tp14.index(3))
print("==========================================================")
#------------------------------------------------------------------

#7. Tuple Membership
tp15 = (5,4,3,2,1)
print(5 in tp15)
print(6 in tp15)
print(6 not in tp15)
print("==========================================================")
#------------------------------------------------------------------

#8. Built-In Functions

#print Length
print(len(tp15))

#Return sorted List
newtp = sorted(tp15)
print(newtp)

#Find max in tuple
print("Mamimum: ", max(tp15))

#Find min in tuple
print("Minimum: ", min(tp15))

#Find sum of a tuple
print("Sum: ", sum(tp15))
print("==========================================================")
#------------------------------------------------------------------