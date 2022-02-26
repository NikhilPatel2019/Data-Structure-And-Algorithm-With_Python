class Stack:
  def __init__(self):
    self.items = []

  def push(self,data):
    self.items.append(data)

  def pop(self):
    return self.items.pop()

  def peek(self):
    if len(self.items) == 0:
      print("Stack is Empty")

    else:
      print("Top Item = ", self.items[-1])

  def print(self):
    for d in self.items:
      print(d, end =" ")
    print()

def rev_string(str):
  st = Stack()
  for i in range(len(str)):
    st.push(str[i])

  rev = ""
  for i in range(len(str)):
    rev += st.pop()
  print(rev)

s = "Namaste"
rev_string(s)