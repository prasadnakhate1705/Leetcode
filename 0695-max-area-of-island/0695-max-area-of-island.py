class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        
        max_area = 0

        def dfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1 or grid[r][c]==0 or grid[r][c]==-1:
                return 0

            grid[r][c]=-1
                
            area = 1+ dfs(r-1,c) + dfs(r,c+1) + dfs(r+1,c)+ dfs(r,c-1)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area = dfs(i,j)
                    max_area = max(max_area, area)

        return max_area            


        