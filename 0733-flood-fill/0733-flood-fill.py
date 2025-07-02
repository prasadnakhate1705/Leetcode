class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        visited = {(sr, sc)}
        og_color = image[sr][sc]
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        if og_color == color:
            return image

        def dfs(i, j, color):

            image[i][j]=color
            visited.add((i,j))

            for x,y in directions:
                if 0<=i+x<rows and 0<=j+y<cols and image[i+x][j+y]==og_color and (i+x, j+y) not in visited:
                    dfs(i+x, j+y,color)


        dfs(sr,sc,color)

        return image            



        