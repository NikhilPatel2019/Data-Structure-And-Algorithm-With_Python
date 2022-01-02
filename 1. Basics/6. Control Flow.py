#Control FLow
#------------------------------------------------------------------
#1. if Statement
num = 10
if num > 10:
  print('Number is greater than 10')
print('This will always be printed')

if None: #None matlab 0 or false
  print("Inside")

if False: #False means -> false
  print("Inside 2")
  #----------------------------------------------------------------

#----------------------------------------------------------------
#2. if else statement
num2 = 20
if num2 > 0:
  print("Positive Number")
else:
  print("Negative Number")
#------------------------------------------------------------------

#------------------------------------------------------------------
#3. if elif else Statement
num3 = 0
if num3 > 0:
  print("Positive Number")
elif num3 == 0:
  print("Zero")
else:
  print("Negative Number")
#------------------------------------------------------------------

#------------------------------------------------------------------
#4. Nested if statement
num4 = 14
if num4 >= 0:
  if num4 == 0:
    print("ZERO")
  else:
    print("Positive Number")
else:
  print("Negative Number")
#------------------------------------------------------------------

#------------------------------------------------------------------
#5. Largest among three numbers
x = 10
y = 50
z = 15
if (x >= y) and (x >= z):
  largest = x
elif (y >= x) and (y >=z):
  largest = y
else:
  largest = z
print("Largest among three numbers is {}".format(largest))
#------------------------------------------------------------------

#------------------------------------------------------------------
#6. While Loop
lst = [10, 20, 30, 40, 50]
product = 1
index = 0
print("List Length: ", len(lst))
while index < len(lst):
  product *= lst[index]
  index += 1
print("Product: {}".format(product))
#------------------------------------------------------------------

#------------------------------------------------------------------
#6. While Loop with else statement
numbers = [1, 2, 3, 4, 5]
index = 0
print("List Length: ", len(lst))
while index < len(numbers):
  print(numbers[index])
  index += 1
else:
  print("No items left in the list")
#------------------------------------------------------------------

#------------------------------------------------------------------
#6. For Loop
lst2 = [1, 2, 3, 4, 5]
product = 1
for ele in lst2:
  product *= ele
print("Product: ", product)
#------------------------------------------------------------------

#------------------------------------------------------------------
#7. For Loop with range()
#default step is 1
for ele in range(10):
  print(ele)

#With steps
print("PRINTING Number form 0 to 20 with 2 step jumps")
for ele in range(1,20,2):
  print(ele)

#With List of strings
lst3 = ["Dolly", "Sunny", "Nikki", "Hemani"]
for index in range(len(lst3)):
  print(lst3[index])
#||||
#With List of strings Simplified
for ele in lst3:
  print(ele)
#------------------------------------------------------------------

#------------------------------------------------------------------
#8. For loop with else
nums = [1,2,4]
for ele in nums:
  print(ele)
else:
  print("No item left")
#------------------------------------------------------------------

#------------------------------------------------------------------#9. break
nums2 = [1,2,3,4,5]
for ele in nums2:
  if ele == 4:
    break
  print(ele)
else:
  print("IN ELSE BLOCK")
print("Outside of for LOOP")
#------------------------------------------------------------------

#------------------------------------------------------------------
#10. continue
nums3 = [1,2,3,4,5]
for num in nums3:
  if num % 2 == 0:
    continue
  print(num)
else:
  print('ELSE BLOCK')  
#------------------------------------------------------------------