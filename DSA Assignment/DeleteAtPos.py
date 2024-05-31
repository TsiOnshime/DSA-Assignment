class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
     self.head = None

  def insertAtBeginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  
  def deleteAtPosition(self, position):
    
    if self.head is None or position < 1:
      return  
    if position == 1:
      temp = self.head
      self.head = self.head.next 
      temp = None
      return
  
    current = self.head
    count = 1
    while current and count < position:   
      current = current.next
      count += 1
    if not current:
      return  
    node_to_delete = current.next
    current.next = node_to_delete.next
