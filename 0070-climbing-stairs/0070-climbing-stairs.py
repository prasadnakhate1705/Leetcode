class Solution:

    def climbStairs(self, n: int) -> int:

        dp_table = [-1] * (n+1)
        
        def dpclimbStairs(k):
            if k<=1:
                return 1 
            
            if dp_table[k]!=-1:
                return dp_table[k]
            
            dp_table[k] = dpclimbStairs(k-1) + dpclimbStairs(k-2)

            return dp_table[k]


        return dpclimbStairs(n)
            