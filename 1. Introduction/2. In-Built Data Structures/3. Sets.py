#1. Set creation
s1 = {1,2,3,4,5}
print("s1: ", s1)

#set doesn't allow duplicates. They store only one instance.
s2 = {1,2,1,3,3,1}
print("s2: ",s2)

#we can make set from a list
s3 = set([1, 2, 3, 4, 5])
print("s3: ",s3)
#------------------------------------------------------------------

#2. Add Element to a SET
#we can add single element using add() method and 
#add multiple elements using update() method
s4 = {1, 2, 3}

#set object doesn't support indexing
# print(s4[1]) 
#will get TypeError

#add Element
s4.add(4)
print("s4: ",s4)

#add multiple elements
s4.update([7,8,9])
print("s4: ",s4)

#add list and set
s4.update([5,6], {11,22,33})
print("s4: ",s4)
#------------------------------------------------------------------

#3. Remove Element from a SET
#A particular item can be removed from set using methods, 
#discard() and remove().
s5 = {1,2,3,4,5,6,7}
print("s5: ",s5)
s5.discard(3)
print("s5: ",s5)

s5.remove(5)
print("s5: ",s5)

#s5.remove() #Will give key error

s5.discard(5)
print("s5: ",s5)

s5.pop() #will pop random element
print("s5: ",s5)

s5.clear()
print("s5: ",s5)
#------------------------------------------------------------------

#4. Set Operations

#UNION (|)
s6 = {5,4,3,2,1}
s7 = {1,2,4,8,9,6}
print("s6 U s7 = ",s6 | s7)
print("Using Union function: ",s6.union(s7))

#INTERSECTION
print("Intersection: ", s6&s7)
print("Using Intersection FUnction: ", s6.intersection(s7))

#set Difference: set of elements that are only in set1 but not in set2
print("Set Difference: ",s6-s7)
print("Set Difference Using function: ",s6.difference(s7))

#symmetric difference: set of elements in both set1 and set2 
#except those that are common in both.
#use ^ operator
print("Symmetric Difference: ",s6^s7)
print("Symmetric Difference Using Function: ",s6.symmetric_difference(s7))

#isSubset()
s8 = { 1, 2, 3, 4, 5, 6}
s9 = { 1, 2}
print("Is s8 subset of s9? ", s8.issubset(s9))
print("Is s8 superset of s9? ", s8.issuperset(s9))
print("Is s9 subset of s8? ", s9.issubset(s8))
print("Is s9 superset of s8? ", s9.issuperset(s8))
#------------------------------------------------------------------

#5. Frozen Sets
s10 = frozenset([1, 2, 3, 4])
s11 = frozenset([3, 4, 5, 6])

#try to add element into set1 gives an error
# s10.add(5)

# frozen set doesn't support indexing
#print(s11[1])

print("Union of frozen sets: ", s10|s11)
print("Intersection of frozen sets: ", s10&s11)
print("Difference of frozen sets: ", s10-s11)
print("Symmetric Difference of frozen sets: ", s10^s11)
#------------------------------------------------------------------