#1. How to import module
import example

#2. Using function inside a module
print(example.add(2,3))

#3. math module
import math
print(math.pi)

#4. datetime module
import datetime
temp = datetime.datetime.now()
print(temp)

#5. import with renaming
import math as m
print(m.pi)

#6. form...import
from datetime import datetime
print(datetime.now())

#7. import all names
from math import *
print(pi)

#8. dir() function
print(dir(example))