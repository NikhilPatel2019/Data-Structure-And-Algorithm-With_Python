def seq(num):
  """
  Given Function prints numbers starting from 0 to number passed as an argument
  """
  for i in range(num):
    print(i)
  return

seq(6)

#Debugging seq()
import pdb

#interactive debugging
def seq2(num):
  """
  Given Function prints numbers starting from 0 to number passed as an argument
  """
  for i in range(num):
    pdb.set_trace() #breakpoint
    print(i)
  return

#list - will tell you where you are in a program
#p - print
#p locals()
#p globals()
#c - continue
#h - help
seq2(6)

#https://web.stanford.edu/class/physics91si/2013/handouts/Pdb_Commands.pdf