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

    def deleteAfterNode(self, prev_node):
       
        if self.head is None or prev_node.next is None:
            print("The node to be deleted after does not exist!")
            return
        node_to_delete = prev_node.next 
        prev_node.next = node_to_delete.next

     
