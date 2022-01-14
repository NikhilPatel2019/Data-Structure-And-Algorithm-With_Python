def hcf(num1, num2):
  """
  Program to find HCF of TWO Numbers
  """

  smallestNum = num1 if num1<num2 else num2
  hcf = 1

  for i in range(1, smallestNum+1):
    # print(i)
    if (num1 % i == 0) and (num2 % i == 0):
      hcf = i
  
  return hcf

x = 25
y = 5
print("HCF of {0} and {1} = {2}".format(x,y,hcf(x,y)))