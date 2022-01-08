#STRING CREATION
print("STRING CREATION:")

s1 = "Namaste"
print("s1: ", s1)

s2 = 'Namaste'
print("s2: ", s2)

s3 = '''Namaste'''
print("s3: ", s3, "\n")
#------------------------------------------------------------------

#ACCESSING STRING CHARACTERS
print("ACCESSING STRING CHARACTERS:")
s4 = 'Namaste'
print(s4[0])
print(s4[-1])
print(s4[2:7], "\n")

#Below accessing will give Error
#print(s4[7])
#print(s4[2.5])
#------------------------------------------------------------------

#CHANGE/DELETE STRING
print("CHANGE/DELETE STRING:")
#String are immutable means you cannot change CHARACTERS
#So Given command will give ERROR s4[1] = 'W'

s5 = 'namaste'
del s5 
# print(s5)
#------------------------------------------------------------------

#STRING OPERATIONS
print("\nSTRING OPERATIONS:")

#1. Conatenatoin
s6 = "Kem"
s7 = "Che"
print(s6 + " " + s7)
print(s6 * 4)

#2.Iterating Through the String
s8 = "onomotopia"
vowels = 0
for l in s8:
  if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' :
    vowels+=1

print("Vowels Count = ", vowels)

#3. Membership Operator
print('a' in s8)
print('z' in s8)

#4. Methods
s9 = "Testing"
print(s9.lower())
print(s9.upper())
print("Splitting Words in a List".split())
print(' '.join(['Join', 'this', 'given', 'list.']))

s10 = "Kuch Bhi"
print(s10.find('hi'))

s11 = "Happy Diwali"
s12 = s11.replace("Diwali", "New Year")
print(s12)
#------------------------------------------------------------------
