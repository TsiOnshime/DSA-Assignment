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

  def insertAtEnd(self, data):
    new_node = Node(data) 
    if self.head is None: 
      self.head = new_node
      return

    last = self.head  
    while last.next: 
      last = last.next
    last.next = new_node  

  def insertAtPos(self, data, position):

    if position < 0: 
      print("Invalid position! Please enter a position 0 or greater.")
      return

    new_node = Node(data) 
    if self.head is None or position == 0:
      self.insertAtBeginning(data)
      return

   
    current = self.head
    count = 1
    while current and count < position:
      current = current.next
      count += 1


    if not current:
      print("Invalid position! The position is greater than the list length.")
      return

    
    new_node.next = current.next
    current.next = new_node

  def printList(self):
    """
    Prints the contents of the linked list in a human-readable format.
    """
    temp = self.head  
    while temp: 
      print(temp.data, end=" -> ") 
      temp = temp.next  
    print("None")  


llist = LinkedList()
llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(3)
llist.insertAtPos(4, 1)  # Insert 4 at position 1
print("Linked list after insertion at position 1:")
llist.printList()
