#1. Default Arguments
def fun1(name, msg="Welcome"):
  print("{} {}".format(msg,name))

fun1('badluram')
fun1('badkuram', 'amar rahe')
#--------------------------------------------------------

#2. Keyword Arguments
def fun2(**kwargs):
  if kwargs:
    print("{0} {1}".format(kwargs['name'],kwargs['msg']))

fun2(name='Badluram',msg='ka badan zamin ka nichey hain...')
#--------------------------------------------------------

#3. Arbitrary Arguments
def fun3(*gana):
  """
  This Function prints tuples items
  """
  for words in gana:
    print(words)
  
fun3('Toh humein uska ration milta hain ...')
print('sabashh... hallelujah....')
#--------------------------------------------------------

