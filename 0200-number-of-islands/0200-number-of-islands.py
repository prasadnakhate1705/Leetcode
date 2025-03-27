from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands=0

        # def dfs(i,j):

        #     if  i<0 or i>rows-1 or j<0 or j> cols-1 or grid[i][j]=='0':
        #         return 

        #     grid[i][j] = '0'    

        #     dfs(i + 1, j)  # Down
        #     dfs(i - 1, j)  # Up
        #     dfs(i, j + 1)  # Right
        #     dfs(i, j - 1)  # Left


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1':  # Found an island
        #             islands += 1
        #             dfs(r, c)  # Sink the entire island

        # return islands        

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = '0'

            while queue:
                m,n = queue.popleft()

                for nr, nc in direction:
                    i,j = m+nr, n+nc
                    if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
                        queue.append((i,j))
                        grid[i][j]='0'


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found an island
                    islands += 1
                    bfs(r, c)

        return islands        
            
        

            



        
        