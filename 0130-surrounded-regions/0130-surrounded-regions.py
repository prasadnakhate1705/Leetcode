class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        directions= [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j):

            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return

            
            board[i][j] = 'T'    

            for x, y in directions:
                    dfs( i+x , j +y)


        for i in range(rows):
            if board[i][0] == 'O':  # Left border
                dfs(i, 0)
            if board[i][cols - 1] == 'O':  # Right border
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == 'O':  # Top border
                dfs(0, j)
            if board[rows - 1][j] == 'O':  # Bottom border
                dfs(rows - 1, j)
                     

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':  
                    board[i][j] = 'X'  # Convert completely surrounded 'O' to 'X'
                elif board[i][j] == 'T':  
                    board[i][j] = 'O'  
          








        