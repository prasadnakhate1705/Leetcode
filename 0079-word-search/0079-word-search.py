class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Four Directions
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        # Visited set to make sure we donot read a letter twice
        visited = set()
        
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, index):
            if len(word)==index:
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] != word        [index]:
                return False

            
            visited.add((r,c))

            for i,j in directions:
                    if backtrack(r+i, c+j, index+1):
                        return True
                
            visited.remove((r,c))
            return False
        
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True

        return False
                

        
        