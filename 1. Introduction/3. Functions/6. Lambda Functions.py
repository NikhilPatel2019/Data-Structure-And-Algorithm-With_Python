#1. Example
double = lambda x: x*2
print("double(4) = ", double(4))

#2. With filter()
l1 = [1,2,3,4,5]
evens = list(filter(lambda x: x%2 == 0, l1))
print("Evens: ",evens)

#3. With map()
l2 = [5,4,3,2,1]
l2_cubed = list(map(lambda x: x**3,l2))
print("l2 Cubed:", l2_cubed)

#4. With reduce()
from functools import reduce
l3 = [10,20,30,40] #total=100
l3_total = reduce(lambda x,y: x+y, l3)
print("l3 Total:",l3_total)