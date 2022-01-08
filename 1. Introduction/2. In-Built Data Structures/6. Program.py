#1. Program to check if a string is palindrome not
st1 = "gamag"

#Convert string to lowercase
st1.lower()

#Store reverse string in another string
revst1 = reversed(st1)

#This will not work as both the string are pinting to a different memory locations
if st1 == revst1:
  print("YES")

#So we need to convert it to list
if list(st1) == list(revst1):
  print("PALINDROME")
else:
  print("NOT PALINDROME")

#2. Program to sort Words in alphabetic Order
st2 = "One Day At A Time"

#Store the string words in a List
words = st2.split()
print(words)

#Sort the list
words.sort()

#Print sorted list
for w in words:
  print(w)
