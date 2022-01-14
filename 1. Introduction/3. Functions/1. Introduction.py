#1. Function Definition
def fun1(arg):
  """
  This Function will print the arguments passed
  """
  print(arg)

#2. Function Calling
fun1('Function Called')

#3. Accessing Function Doc String
print(fun1.__doc__)

#4. return Statement
def fun2(l):
  sum = 0
  for num in l:
    sum += num
  return sum

res = fun2([1,2,3,4,5]) 
print(res)

#5. Scope of variables
globalVariable = 100

def fun3():
  loacalVariable = 20
  print("Globa Variable", globalVariable)
  print("Local Variable", loacalVariable)

fun3()
print("Global Variable", globalVariable)
#This will give error as scope of local variable is inside a function
#print(loacalVariable)