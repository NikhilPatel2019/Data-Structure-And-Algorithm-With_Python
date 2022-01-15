def factorial(num):
  """
  Recursive function to find the factorial of a given number
  """
  return 1 if num == 1 else (num * factorial(num-1))

num = 4
print("{0}! = {1}".format(num, factorial(num)))

#-----------------------------------------------------------

def fibonacci(num):
  """
  Recursive function to print fibonacci sequence
  """
  return num if num <=1 else fibonacci(num-1) + fibonacci(num - 2)

terms = 10
for num in range(terms):
  print(fibonacci(num))
