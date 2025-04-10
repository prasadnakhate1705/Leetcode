
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph)-1
        #visited = set()
        output = []

        def dfs(node, path):
            
                

            path.append(node)
            #visited.add(node)

            if node == target:
                output.append(path.copy()) 

            for i in  graph[node]:
                # if i not in visited:
                #     dfs(i, path)
                dfs(i, path) 

            #visited.remove(node)
            path.pop() 

        dfs(0, [])

        return output                   

                






        


        