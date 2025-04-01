class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):

            isConnected[city][city]==-1

            for neighbour in range(len(isConnected)):
                if isConnected[city][neighbour]==1:
                    isConnected[city][neighbour] = -1  
                    isConnected[neighbour][city] = -1  
                    dfs(neighbour)

        province = 0

        for city in range(len(isConnected)):
            if  isConnected[city][city]!=-1:
                dfs(city)
                province+=1

        return province        

        