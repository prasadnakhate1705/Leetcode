class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # directions =[(1,0), (0,1)] # Right and down

        # rows = len(grid)
        # cols = len(grid[0])

        # # For memoziation
        # matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        # def dp(r,c):
        #     if r >= rows or c >= cols:
        #         return float('inf')

        #     if r == rows - 1 and c == cols - 1:
        #         return grid[r][c] 
            
        #     # Already stored in the Dp memo array
        #     if matrix[r][c] != -1:
        #         return matrix[r][c]
            
        #     # two options right and down
        #     right = dp(r, c + 1)
        #     down = dp(r + 1, c)

        #     #Update the table
        #     matrix[r][c] = grid[r][c] + min(right, down)

        #     return matrix[r][c]

        #return dp(0,0)
        
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0]
        
        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    dp[r][c] = min(dp[r][c], dp[r-1][c] + grid[r][c])
                if c > 0:
                    dp[r][c] = min(dp[r][c], dp[r][c-1] + grid[r][c])


        return dp[-1][-1]



        
            







        

        