class Node:
  def __init__(self, data= None, next = None ):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def print(self):
    if self.head == None:
      print("Linked List Is Empty")
      return
    itr = self.head
    while itr:
      print(itr.data , ' --> ' , end =" ")
      itr = itr.next
    print("None")

  def length(self):
    if self.head == None:
      print("Linked List is Empty")
      return
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    print("Length =", count)
    return count
  def insert_at_end(self, data):
    if self.head == None:
      self.head = Node(data,None)
      return
    itr = self.head

    while itr.next:
      itr = itr.next

    itr.next = Node(data,None)

  def insert_at_beginning(self,data):
    if self.head == None:
      self.head = Node(data,None)
      return
    newNode = Node(data, None)
    newNode.next = self.head
    self.head = newNode

  def insert_at(self,position,data):
    if position <0 or position > self.length():
      print("Invalid Index")

    if position == 0:
      self.insert_at_beginning(data)
      return

    count = 0
    itr = self.head
    while itr:
      if count == position-1:
        node = Node(data,itr.next)
        itr.next = node
        break

      itr = itr.next
      count += 1

  def remove_at(self,position):
    if position < 0 or position > self.length():
      print("Invalid Syntax")

    if position == 0:
      self.head = self.head.next
      return

    count = 0
    itr = self.head
    while itr:
      if count == position-1:
        itr.next = itr.next.next
        return
      count += 1
      itr = itr.next

  def insert_list(self,dataList):
    self.head = None
    for d in dataList:
      self.insert_at_end(d)
      
ll = LinkedList()
ll.insert_at_end(8)
ll.insert_at_end(5)
ll.insert_at_beginning(9)
ll.insert_at_beginning(15)
ll.insert_at_end(10)
ll.insert_at(2,6)
ll.remove_at(3)

# ll.insert_list([9,6,8,7,10,5,4,3,2,1])

ll.print()

