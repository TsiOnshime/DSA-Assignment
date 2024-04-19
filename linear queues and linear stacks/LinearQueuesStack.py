class LinearQueuesStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self,element):
        self.enqueue_stack.append(element)
    def dequeue(self):
        if len(self.dequeue_stack) == 0:
           while len(self.enqueue_stack) > 0:
             self.dequeue_stack.append(self.enqueue_stack.pop())
        if len(self.dequeue_stack) == 0:
          return None  

        return self.dequeue_stack.pop()
    def peek(self):
        if len(self.dequeue_stack) == 0:
          while len(self.enqueue_stack) > 0:
              self.dequeue_stack.append(self.enqueue_stack.pop())


        if len(self.dequeue_stack) == 0:
          return None  

        return self.dequeue_stack[-1] 

    def isEmpty(self):
        if len(self.enqueue_stack)== 0 and len(self.dequeue_stack) ==0:
            return True
        return False
    def isFull(self):
        if len(self.enqueue_stack) + len(self.dequeue_stack) == self.capacity:
            return True
        return False


QS = LinearQueuesStack()
    
    