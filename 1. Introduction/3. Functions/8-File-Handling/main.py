#1. Opening a FILE
f1 = open('example.txt')
# print(f) #try this out
#-------------------------------------------------------------

#2. Python FILE modes
#read mode
f2 = open('example.txt') #read mode is default
f3 = open('example.txt', 'r')
#open in  write mode
f4 = open('example.txt', 'w')
#------------------------------------------------------------

#3. Closing a file
f4.close()
f3.close()
f2.close()

#Using try and finally
try:
	f = open('example.txt')
finally:
	f.close()
#We don’t need to explicitly call the close() method. It is done internally.
#---------------------------------------------------------------

#4. Writing to a file
f5 = open('example.txt', 'w')
f5.write("Testing write mode\n")
f5.write("Writing again...")
f5.close()
#----------------------------------------------------------------

#5. Reading from a file
f6 = open('example.txt','r')
print(f6.read())

f7 = open('example.txt','r')

#Cursor is at the start
temp = f7.read(7)
print("Temp1: ",temp)

#Now cursor is at 7 position
temp2 = f7.read(8)
print("Temp2: ",temp2)

#Will return current position of a cursor
print(f7.tell())

#Bring the file cursor to an initial position
print(f7.seek(0))

#Reading a file using foor loop - print line in each iteration
for line in f7:
  print(line)

#alternate method using readline() method
f8 = open('example.txt','r')
print(f8.readline())
#------------------------------------------------------------

#6. Renaming and deleting a file
import os

os.rename('example.txt', 'testfile.txt')

#deleting a file
#os.remove('testfile.txt')
#-----------------------------------------------------------

#7. Working with directory
import os
print(os.getcwd())

#changing directory
os.chdir('/home/runner')
print(os.getcwd())

#Getting list of all items in a directory
print(os.listdir(os.getcwd()))

#will remove empty directory
os.chdir('/home/runner/8-File-Handling')
# os.mkdir('test')
# os.rmdir('test')

#will remove non-empty directory
import shutil
# os.mkdir('test2')
os.chdir('./test2')
f = open("testFile.txt",'w')
f.write("Hello There")
os.chdir('../')

# os.rmdir('test') #this will give an error

#will remove non-empty directory
shutil.rmtree('test2')
#----------------------------------------------------------------