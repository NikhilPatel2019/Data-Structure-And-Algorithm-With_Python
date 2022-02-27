class Queue:
  q = []
  front = rear = None

  def isEmpty(self):
    if len(self.q) == 0:
      return True
    else :
      return False

  def print(self):
    for data in self.q:
      print(data, end = " ")
    print()

  def enqueue(self,data):
    self.q.append(data)
    if len(self.q) == 1:
      front = rear = 0
    else:
      r = len(self.q) - 1

  def dequeue(self):
    if self.isEmpty():
      print("UnderFlow!!")
    else:
      poppedItem = self.q.pop(0)
      print(poppedItem, "popped")
    if len(self.q) == 0:
      front = rear = None

  def peek(self):
    if self.isEmpty():
      print("Underflow")
    else:
      print("Top = ",self.q[0])
      
q1 = Queue()
q1.enqueue(34)
q1.enqueue(56)
q1.enqueue(67)
q1.enqueue(89)
q1.print()
q1.dequeue()
q1.dequeue()
q1.print()
q1.peek()