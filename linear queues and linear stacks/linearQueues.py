class LinearQueues:
    def __init__(self):
        self.list= []
        self.front= 0
        self.rear= 0
        self.capacity = 8 # let our queue hava a capacity of 8
        self.size = 0 
    def isEmpty(self):
        if self.front== self.rear:
            return True
        else:
            return False
        
    def isFull(self):
        if self.size == self.capacity:
            return True
        else:
            return False
    def enqueue(self,n):
        if self.isFull():
            print("we can't add a new element")
        else:
            self.list.append(n)
            self.rear +=1
            self.size +=1
            
    def dequeue(self):
        if self.isEmpty():
            print("no element to be removed")
        else:
            del self.list[self.front]
            self.size -= 1
    def peek(self):
        if self.size > 0:
            return self.size[self.rear]
queue= LinearQueues()

    