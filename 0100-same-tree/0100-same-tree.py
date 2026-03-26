# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(temp1, temp2):
            if not temp1 and not temp2:
                    return True
            
            if not temp1 or not temp2:
                    return False

            if temp1.val!=temp2.val:
                return False
            
            return dfs(temp1.left, temp2.left) and dfs(temp1.right, temp2.right)
            
    
        
        return dfs(p,q)
            

        