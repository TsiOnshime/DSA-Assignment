class CircularQueues:
    def __init__(self):
        self.list= []
        self.front= 0
        self.rear= 0
        self.capacity = 8 # let our queue hava a capacity of 8
        self.size = 0 
  
    def enqueue(self,element):
        if self.isFUll():
            return False
        self.list[self.rear] = element
        self.size += 1
        self.rear = (self.rear +1 )% self.capacity
        
        
    def dequeue(self):
        if self.isEmpty():
            return False
        self.size -= 1
        self.head = (self.head + 1 ) % self. capacity
    
    def Front(self):
        if self.isEmpty():
            return -1
        return self.list[self.head]
    def Rear (self):
        if self.isEmpty():
            return -1
        return self.list[self.tail-1]
    def isEmpty(self):
        if self.size == 0 :
            return True
        return False
    def isFull(self):
        if self.size == self.capacity:
            return True
        return False
cir_q = CircularQueues()
         
            
    
    
    

    