class Solution:
    def fib(self, n: int) -> int:

        mem = [0]*(n+1)

        def recursion(n):
            if n==0:
                return 0
                
            if n==1:
                return 1
            
            if mem[n]!=0:
                return mem[n]
            
            mem[n] = recursion(n-1) + recursion(n-2) 

            return mem[n] 
        
        return recursion(n)

        