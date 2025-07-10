class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions= [(1,0),(0,1), (-1,0), (0,-1), (1,1),(1,-1),(-1,-1),(-1,1)]
        n =len(grid)

        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        if n==1:
            return 1

        
        q = deque([])
        q.append((0,0,1))
        grid[0][0] = 1

        while q:
            i, j, path = q.popleft()

            for di,dj in directions:
                ni,nj = di+i, dj+j 

                if 0<= ni<n and 0<=nj<n and grid[ni][nj]==0:
                    if ni == n-1 and nj == n-1:
                        return path+1

                    grid[ni][nj]=1
                    q.append((ni,nj,path+1))

        return -1
    

            
        