class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [(-1,0), (0,1), (1,0),(0,-1)]

        present_color = image[sr][sc]

        if present_color == color:
            return image

        def dfs(i, j):
            
            image[i][j]=color

            for x, y in directions:
                if 0<= i+x <len(image) and 0<= j+y<len(image[0])  and image[i+x][j+y]             ==present_color:
                    dfs(i+x, j+y)  

        dfs(sr,sc)

        return image    

        