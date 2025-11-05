class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions =[(1,0), (0,1)]

        rows = len(grid)
        cols = len(grid[0])
        matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        def dp(r,c):
            if r >= rows or c >= cols:
                return float('inf')

            if r == rows - 1 and c == cols - 1:
                return grid[r][c] 
            
            if matrix[r][c] != -1:
                return matrix[r][c]
            
            right = dp(r, c + 1)
            down = dp(r + 1, c)

            matrix[r][c] = grid[r][c] + min(right, down)

            return matrix[r][c]
        
        
        
        return dp(0,0)
            







        

        