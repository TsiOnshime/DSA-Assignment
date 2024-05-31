class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # I added insertAtBeginning function just to 
    # add elements to the linked list and check 
    # if my search function works
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def searchNode(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current # returns the location of the node
            current = current.next
        return "Node not found" 
    
    
LL= LinkedList()
LL.insertAtBeginning(4)
LL.insertAtBeginning(2)
LL.insertAtBeginning(3)
print(LL.searchNode(3))
