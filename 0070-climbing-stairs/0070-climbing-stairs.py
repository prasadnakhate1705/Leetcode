class Solution:

    def climbStairs(self, n: int) -> int:

        memo = [-1] * (n+1)
        
        def dp(k):
            if k<=1:
                return 1 
            
            if memo[k]!=-1:
                return memo[k]
            
            memo[k] = dp(k-1) + dp(k-2)

            return memo[k]

        ans = dp(n)

        return ans
            