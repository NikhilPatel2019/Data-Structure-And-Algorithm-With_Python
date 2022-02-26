class Stack:
  def __init__(self):
    self.items = []

  def push(self,data):
    self.items.append(data)

  def pop(self):
    poppedItem = self.items.pop()
    print(poppedItem, "popped")

  def peek(self):
    if len(self.items) == 0:
      print("Stack is Empty")

    else:
      print("Top Item = ", self.items[-1])

  def print(self):
    for d in self.items:
      print(d, end =" ")
    print()

users = Stack()

users.push(9)
users.push(56)
users.push(98)
users.push(55)

users.print()

users.pop()

users.print()

users.peek()