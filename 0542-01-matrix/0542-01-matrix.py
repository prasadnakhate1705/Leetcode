class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, cols = len(mat), len(mat[0])

        ans = [[-1] * cols for _ in range(rows)]

        q = deque()

        ## append all the zeroes in the queue
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    ans[i][j]=0
                    q.append((i,j))

        while q:

            i,j = q.popleft()
            for di, dj in directions:
                ni,nj = i+di, j+dj

                if 0<= ni < rows and 0<=nj< cols  and ans[ni][nj]==-1:
                    ans[ni][nj]= ans[i][j]+1
                    q.append((ni,nj))
        
        return ans

                
                    
        
        return ans






        