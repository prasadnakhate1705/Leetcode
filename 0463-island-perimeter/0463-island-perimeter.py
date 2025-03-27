class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,col = len(grid), len(grid[0])
        #visited = set()

        # dfs function to check four dirction
        def dfs(r,c):

            # add 1 for the following conditions
            if r<0 or r>=rows or c>=col or c<0 or grid[r][c]==0:
                return 1

            # If already visited
            if grid[r][c]==-1:
                return 0

            # Mark Visited
            grid[r][c]=-1

            perimeter = (dfs(r - 1, c) +  # Up
                     dfs(r + 1, c) +  # Down
                     dfs(r, c - 1) +  # Left
                     dfs(r, c + 1))   # Right
            return perimeter  

        #find the first 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)

        return 0                   


        

        