class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## Placing N Queens on the Board

        col = set()
        posdiag = set() #r+c
        negdiag = set() #r-c

        # Empty Board
        board = [['.']*n for i in range(n)]
        
        result = []  #Final result to share

        def backtrack(r):
            # Base condition
            if r==n:
                result.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue

                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                #backtrack and undo the changes for that row.
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]="."
        
        backtrack(0)

        return result
                
                

        
