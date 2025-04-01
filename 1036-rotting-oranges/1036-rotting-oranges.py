from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        queue = deque()
        fresh_count = 0
        rows, cols = len(grid), len(grid[0])

        ## first append the rotten oranges to the queue
        ## count the fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        ## Base Case
        if fresh_count == 0:
            return 0
        
        minutes = 0

        ## travering the queue
        while queue:
            minutes += 1  # Increment time at each level
            for _ in range(len(queue)):  # Process all oranges in the current level
                i, j = queue.popleft()
                for x, y in directions:
                    ni, nj = i + x, j + y
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2  # Rot the orange
                        fresh_count -= 1
                        queue.append((ni, nj))
        

        return minutes - 1 if fresh_count == 0 else -1                     

                    

                


        