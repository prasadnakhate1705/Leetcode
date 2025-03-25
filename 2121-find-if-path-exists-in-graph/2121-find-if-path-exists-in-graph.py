from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        visited = set()

        adj_list = defaultdict(list)

        for i in range(len(edges)):
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])

        def dfs(node):
            if node == destination:
                return True    
            visited.add(node)

            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True

            return False        

        ans = dfs(source) 

        return ans   

        