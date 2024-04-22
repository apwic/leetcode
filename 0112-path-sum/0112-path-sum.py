# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
           
        def DFS(node, curr):
            if node == None:
                return False
            
            curr += node.val
            if curr == targetSum and (node.left == None) and (node.right == None) :
                return True
            
            if DFS(node.left, curr) or DFS(node.right, curr):
                return True
        
        return DFS(root, 0)