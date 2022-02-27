class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLL:
  def __init__(self):
    self.head = None

  def print(self):
    if self.head is None:
      print("Linked List is Empty")
    else:
      itr = self.head 
      while itr:
        print(itr.data, " --> ", end=" " )
        itr = itr.next
      print("None")

  def length(self):
    count = 0 
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    return count

  def insert_at_beginning(self,data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      return
    temp = self.head
    temp.prev = newNode
    newNode.next = temp
    self.head = newNode

  def insert_at_end(self,data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      return

    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = newNode
    newNode.prev = itr

  def insert_at(self,position,data):
    if position < 0 or position > self.length():
      print("Invalid Index")
      return
    if position == 0:
      self.insert_at_beginning(data)
    else:
      itr = self.head
      count = 0
      while itr.next:
        if count == position-1:
          newNode = Node(data)
          newNode.next = itr.next
          newNode.prev = itr
          itr.next = newNode
          break
        count += 1
        itr = itr.next

  def remove_at_beginning(self):
    self.head = self.head.next

  def remove_at_end(self):
    itr = self.head.next
    before = self.head
    while itr.next is not None:
      itr = itr.next
      before = before.next
    itr.prev = None
    before.next = None
    

  def remove_at(self,position):
    if position < 0 or position > self.length():
      print("Invalid Index")
    if position == 0:
      self.remove_at_beginning()
    else:
      itr = self.head
      count = 0
      while itr.next:
        if count == position-1:
          temp = itr.next.next
          itr.next = itr.next.next
          temp.prev = itr
        count += 1
        itr = itr.next

    
ll = DoublyLL()
ll.insert_at_beginning(90)
ll.insert_at_beginning(80)
ll.insert_at_end(70)
ll.insert_at_end(60)
ll.print()

ll.insert_at(2,50)
ll.print()

ll.remove_at_end()
ll.print()
print("Length = ",ll.length())