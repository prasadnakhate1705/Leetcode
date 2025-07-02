from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # '1' - Land
        # '0' - Water
        rows, cols = len(grid), len(grid[0])
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        islands =0

        def bfs(i,j):
            q = deque([(i,j)])
            grid[i][j]='0'
            

            while q:
                i,j = q.popleft()
                for di, dj  in direction:
                    x,y = i+di, j+dj
                    if 0<=x<rows and 0<=y<cols  and grid[x][y]=='1':
                        grid[x][y]='0'
                        q.append((x,y))
                        


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    islands+=1
                    bfs(i,j)
        
        

        return islands                



        