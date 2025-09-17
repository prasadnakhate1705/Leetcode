class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        n = len(cost)
        mem = [-1]*(n+1)

        mem[n] = 0 

        def dp(k):
            if k<=1:
                return cost[k]
            
            if mem[k]!= -1:
                return mem[k]
            
            mem[k] = cost[k] + min(dp(k-1) , dp(k-2)) 

            return mem[k]
        
        return min(dp(n-1), dp(n-2))
        

        
            

            
            
            
        