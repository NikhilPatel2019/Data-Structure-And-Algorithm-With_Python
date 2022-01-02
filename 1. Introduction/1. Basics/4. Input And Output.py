#OUTPUT
print("NAMASTE")

a = 15
print('Value of a is: ', a)

#OUTPUT FORMATTING

#1. Default
b = 25; c = 6
print('Value of b is {} and value of c is {}'.format(b,c))

#2. Specify position of arguments
print('Value of c is {1} and value of b is {0}'.format(b,c))

#3. we can use keyword arguments to format the string
print('Hello {name}, {greetings}'.format(name="Nikhil", greetings="Su Chale!"))

#4. we can combine positional arguments with keyword arguments
print('The story of {0}, {1}, and {other}'.format('Ram', 'Lakhan',other='Rum Pum Pum'))

#INPUT
num = input("Enter a number: ")
print(num)