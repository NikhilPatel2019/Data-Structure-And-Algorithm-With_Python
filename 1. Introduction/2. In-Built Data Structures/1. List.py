#1. List Creation
emptyList = []
lst = ['one', 'two', 'three', 'four'] #List of Strings
lst2 = [1,2,3,4,5] #List of Numbers
lst3 = [[1,2],[3,4]] # List of Lists
lst4 = [1, 'ramu', 2.98, 50 ] # List of different data types
#-----------------------------------------------------------------

#2. List Length
lst5 = [1,2,3,4,5,6]
print("List5 Length = ", len(lst5))
#------------------------------------------------------------------

#3. List Append
lst6 = ['One', 'two', 'three', 'four']
lst6.append('Five')
print("List6: ",lst6)
#-----------------------------------------------------------------

#4. List Insert
lst7 = ['One', 'two', 'four']
lst7.insert(2,'KA')
#For inserting two arguments are needed -> index and value0
print("List7: ",lst7)
#-----------------------------------------------------------------

#5. List Remove -Require Value
lst8 = ['One', 'two', 'three', 'four', 'two']
lst8.remove('two')
#it will remove first occurence of 'two' in a given list
print("List8: ", lst8)
#-----------------------------------------------------------------

#6.List Append And Extend
lst9 = ['One', 'two', 'three', 'four']
lst10 = ['five', 'six']
lst9.append(lst10);
print("List9: ",lst9)

lst11 = ['One', 'two', 'three', 'four']
lst12 = ['five', 'six']
# lst12 = "seven"
#extend will join the list11 with list12
lst11.extend(lst12);
print("List11: ",lst11)
#-----------------------------------------------------------------

#7. List Delete - Require Index
lst13 = ['One', 'two', 'three', 'four', 'five', 'six']
del lst13[3]
print("List13: ",lst13)

#or we can use pop() method
poppedItem = lst13.pop(2)
print("List13 After Popping: ",lst13)
print("Popped Item: '", poppedItem, "'")
#-----------------------------------------------------------------

#8. List Related Keywords In Python
#keyword 'in' is used to test if an item is in a list
lst14 = ['one', 'two', 'three', 'four', 'five', 'six']
if 'four' in lst14:
  print('Line 62: "four" Present In List14')

#keyword 'not' can combined with 'in'
if 'seven' not in lst14:
    print('Line 66: "seven" not present in a list14')
#-----------------------------------------------------------------

#9. List Reverse 
lst15 = ['one','two', 'three', 'four', 'five']
lst15.reverse();
print("List15: ", lst15)
#-----------------------------------------------------------------

#10. List Sorting
lst16 = [7,4,5,9,8,1,3,2]
sortedList = sorted(lst16)
print("SortedList: ", sortedList)
reverseSortedList = sorted(lst16, reverse=True)
print("Reverse sorted list: ", reverseSortedList)
print("List16: ", lst16)

lst16.sort();
print("SortedList16: ", lst16)
#NOTE: SOrting with list data type not allowed
#-----------------------------------------------------------------

#11. List Having Multiple References
lst17 = [1,2,3,4]
lst18 = lst17
lst18.append(101)
print("List17: ", lst17)
#-----------------------------------------------------------------

#12. String Split To Create a List
st = "one,two,three,four,five,six"
slst = st.split(',')
print("String To List: ",slst)

st2 = "Welcome to Python Programming. ."
slst2 = st2.split()
print("Line 103: ", slst2)
#-----------------------------------------------------------------

#13. List Indexing
lst19 = [1,2,4,5,6,7,9,10]
#print 3rd Element
print("List Indexing: ", lst19[2])

#print last Element
print("List Indexing: ", lst19[-1])
#-----------------------------------------------------------------

#14. List Slicing
lst20 = [1,2,3,4,5,6,7,8,9,10,20,30]
print("Print all item of a List: ", lst20[:])

#print from index 0 to index 4
print("Line 120: ", lst20[0:5])

#print alternate elements in a list
print("Line 123: ", lst20[::3])
#print(lst20[::1])
#print(lst20[::2])

#print elemnts start from 3 through rest of the list with step=2
print("Line 128: ", lst20[2::2])
#-----------------------------------------------------------------

#15. List extend using +
lst21 = [1,2,3,4,5]
lst22 = [6,7,8,9,10]
lst23 = lst21 + lst22
print("List23: ", lst23)
#-----------------------------------------------------------------

#16. List Count 
lst24 = [1,2,3,4,5,6,7,8,7,6,5,3,2,1]
#frequency of 8 in a list
print("Line 141: ", lst24.count(8))

#frequency of 7 in a list
print("Line 144: ", lst24.count(7))
#-----------------------------------------------------------------

#17. List Looping 
lst25 = ['five', 'four', 'three', 'two', 'one']
for strnum in lst25:
  print(strnum)
#-----------------------------------------------------------------

#18. List Comprehensions
# without list comprehension
squares = []
for i in range(10):
    squares.append(i**2)   #list append
print("Line 158: ", squares)

#using list comprehension
squares2 = [i**2 for i in range(10)]
print("Line 162: ", squares2)

#example
lst26 = [-10, -20, -30,  10, 20, 30, 40, 50]

#create a new list with values doubled
newlst = [i*2 for i in lst26]
print("Line 169: ", newlst)

#filter the list to exclude negative numbers
newlst2 = [i for i in lst26 if i >= 0]
print("Line 173: ", newlst2)


#create a list of tuples like (number, square_of_number)
newlst3 = [(i, i**2) for i in range(10)]
print("Line 178: ", newlst3)
#-----------------------------------------------------------------

