#Write a code snippet to implement a stack using arrays in your preferred programming language, 
# including push and pop operations.


class Stack:
    def __init__(self, capacity):
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
   
        
s = Stack(5) # let the capacity of our array be 5
s.push(3)
s.push(4)


