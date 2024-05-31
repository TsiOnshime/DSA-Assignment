class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack underflow!")
            return None 
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return None  
        return self.top.data

    def isEmpty(self):
        return self.top is None  
    
    def print_list(self):
       current = self.top
       while current:
            print(current.data, end=" -> ")
            current = current.next
       print("None")
    
stack1=Stack()
stack1.push(1)
stack1.push(3)
stack1.push(5)
stack1.pop()
stack1.peek()
stack1.print_list()