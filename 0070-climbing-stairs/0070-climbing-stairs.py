class Solution:

    def climbStairs(self, n: int) -> int:
        
        # This is similar to Fibbonacci series

        # Memoization
        dp_table = [-1] * (n+1)
        
        def dpclimbStairs(k):
            if k<=1:
                return 1 
            
            if dp_table[k]!=-1:
                return dp_table[k]
            
            dp_table[k] = dpclimbStairs(k-1) + dpclimbStairs(k-2)

            return dp_table[k]
        
        #return dpclimbStairs(n)

        dp_table[0]=1
        dp_table[1]=1

        for i in range(2,n+1):
            dp_table[i] = dp_table[i-1]+ dp_table[i-2]

        
        return dp_table[n]

            