class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        visited = []
        og_color = image[sr][sc]
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def bfs(i, j, color):

            image[i][j]=color
            visited.append([i,j])

            for x,y in directions:
                if 0<=i+x<rows and 0<=j+y<cols and image[i+x][j+y]==og_color and [i+x, j+y] not in visited:
                    bfs(i+x, j+y,color)


        bfs(sr,sc,color)

        return image            



        