"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        queue = deque()
        if not root:
            return None

        node = root
        queue.append(node)

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev= node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        
        return root
                


            
            


        
        