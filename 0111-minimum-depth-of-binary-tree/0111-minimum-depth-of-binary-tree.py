# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, min_val):
            if node == None:
                return
                
            if not node.left and not node.right:
                return min_val 

            left = dfs(node.left, min_val+1)
            right = dfs(node.right, min_val+1)
            
            if left and right:
                return min(left, right)
            
            if left:
                return left

            if right:
                return right
            

        return dfs(root, 1)