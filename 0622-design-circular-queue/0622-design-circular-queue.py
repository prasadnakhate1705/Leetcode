class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.Capacity = k
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.front is None:
            new = Node(value)
            self.front = self.rear = new
            self.size+=1
            return True
        
        if self.size==self.Capacity:
            return False
        new = Node(value)
        self.rear.next = new
        self.rear = new
        self.size+=1
        return True
        
    def deQueue(self) -> bool:
        if self.front is None:
            return False
        
        new = self.front
        if self.front.next:
            self.front = self.front.next
        else:
            self.front= None
            self.rear = None
        del(new)
        self.size-=1
        return True

    def Front(self) -> int:
        if self.front:
            return self.front.val
        else:
            return -1
        
    def Rear(self) -> int:
        if self.rear:
            return self.rear.val
        else:
            return -1
        
    def isEmpty(self) -> bool:
        if self.size==0:
            return True
    
        return False
        
    def isFull(self) -> bool:
        if self.size== self.Capacity:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()