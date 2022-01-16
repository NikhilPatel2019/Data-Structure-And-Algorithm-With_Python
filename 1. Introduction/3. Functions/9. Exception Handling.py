#1.  Syntax error
# print 'hello'

#2. ZeroDivisionError
# 1/0

#3. FileNotFoundError
# open('example.txt')

#4. Built-in exceptions
print(dir(__builtins__))

#5. Using Try and except
import sys
l1 = [0,1,2,'a']

for ele in l1:
  try:
    print("Current Value Is: ", ele)
    temp = 1 * int(ele)

  except:
    print("OOPS! ", sys.exc_info()[0], " occured." )
  
print("EVEN ERROR OCCURED PROGRAM STILL RUNS")

#6. Handling Specific Exception 
l2 = [0, 'a', 1, 2]

for ele in l2:
  try:
    print('------------------------------------------------')
    print("Current Value is:", ele)
    temp = 1 * int(ele)

  except(ValueError):
    print("This is value Error")
  except(ZeroDivisionError):
    print("Division by zero not allowed")
  except:
    print("Other error")

print("HANDLING COMPLETED")

#7. Raising Error
# raise KeyboardInterrupt
# raise MemoryError("This is memory ERROR")

#8. Example
try:
  num = int(input("Enter positive number: "))
  if num <=0:
    raise ValueError("ERROR: Number entered is negative")

except ValueError as e:
  print(e)

