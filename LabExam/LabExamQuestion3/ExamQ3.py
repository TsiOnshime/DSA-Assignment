#Implement a linear queue data structure using two stacks in Java (take the Stacks in question 2),
# where the stacks are implemented using arrays. The implementation should provide functionality for 
# enqueue, 
# dequeue,
# and peek operations,
# adhering to the FIFO (First In, First Out) principle.



class Stack:
    def __init__(self, capacity=5): # let our array's capacity be 5
        self.capacity = capacity  
        self.arr = []  
        self.top = -1 
    def push(self, item):
        if self.isFull():
            return ("Stack is full")
        self.arr.append(item)
        self.top += 1
    def isFull(self):
        if self.top == self.capacity:
            return True
        return False
    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        popped=self.arr[self.top]
        self.top -=1
        return popped
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def peek(self):
        if self.isEmpty():
            return ("None")
        print(self.arr[self.top])
   
        
class QueueUsingStack:
    stack1 = Stack()
    stack2 = Stack ()
    def __init__(self):
       self.stack1 = Stack()
       self.stack2 = Stack()
    def enqueue(self,element):
        if self.stack1.isFull() and self.stack2.isFull():
            return("Queue is Full")
        return(self.stack1.push(element))
    def dequeue(self):
        if self.stack1.isEmpty() and self.stack1.isFull():
            return ("Queue is Empty")
        self.stack2.push(self.stack1.pop())
        dequeued = self.stack2.arr[self.top]
        return dequeued 
    
    def peek(self):
        if self.stack1.isEmpty() and self.stack1.isFull():
            return ("None")
        self.stack1.arr[self.top]
        
Q1 = QueueUsingStack()
Q1.enqueue (3)
Q1.enqueue (4)
Q1.dequeue()
Q1.peek()