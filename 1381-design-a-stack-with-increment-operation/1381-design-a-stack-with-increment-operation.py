class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize= maxSize
        self.currSize = 0
        
    def push(self, x: int) -> None:
        if self.currSize < self.maxSize:
            self.stack.append(x)
            self.currSize+=1
            
    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
            
        if len(self.stack)>0:
            self.currSize-=1
            return self.stack.pop()


    def increment(self, k: int, val: int) -> None:
        
        if k>self.currSize:
            for i in range(self.currSize):
                self.stack[i]+=val
        else:
            for i in range(k):
                self.stack[i]+=val

        
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)