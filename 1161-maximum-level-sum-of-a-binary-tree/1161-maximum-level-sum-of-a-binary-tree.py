# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque()
        queue.append(root)
        res = []

        while(queue):
            sum =0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum = sum+node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            
            res.append(sum)
        
        print(res)

        maxi=res[0]
        idx =0

        for i , ele in enumerate(res):
            if ele > maxi:
                maxi= ele
                idx =i
        
        return idx+1


            



        