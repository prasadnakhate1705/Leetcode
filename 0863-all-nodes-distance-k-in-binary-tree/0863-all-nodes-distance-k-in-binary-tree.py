from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        queue = deque()
        queue.append(root)
        hash_map = {}

        def bfs(node):
            while queue:
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    hash_map[node.left]=node
                if node.right:
                    queue.append(node.right)
                    hash_map[node.right]=node

        bfs(root)
        result = []
        visited = set()
        queue.append((target, 0))
        visited.add(target)

        while queue:

            node, distance = queue.popleft()
            if distance == k:
                result.append(node.val)
                while queue and queue[0][1] == k:
                    result.append(queue.popleft()[0].val)
                return result
                

            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append((node.left, distance + 1))
            
            # Right child
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append((node.right, distance + 1))
            
            # Parent
            if node in hash_map and hash_map[node] not in visited:
                parent_node = hash_map[node]
                visited.add(parent_node)
                queue.append((parent_node, distance + 1))
        
        return []


        
                
                

            


        
            
            

        