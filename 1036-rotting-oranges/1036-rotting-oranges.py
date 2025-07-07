class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 2- rotten orange
        # 1 - fresh orange
        # 0 - empty cell

        self.minutes = 0
        self.fresh=0
        rows , cols = len(grid), len(grid[0])
        direction = [(1,0),(0,1), (0,-1), (-1,0)]

        q = deque()

        def bfs():   
            while q:
                i,j, mini = q.popleft()

                self.minutes= max(self.minutes,mini)

                for di, dj in direction:
                    if 0<=di+i<rows and 0<=dj+j<cols and grid[di+i][dj+j]==1:
                        self.fresh-=1
                        grid[di+i][dj+j]=2
                        q.append((di+i, dj+j,mini+1))

                   

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    self.fresh+=1
                
                if grid[i][j]==2:
                    q.append((i,j,0))

        bfs()  

        if self.fresh>0:
            return -1
                    

        return self.minutes  