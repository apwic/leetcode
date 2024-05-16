# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def DFS(node):
            if node.val == 0 or node.val == 1:
                return node.val
            
            if node.val == 2:
                return DFS(node.left) or DFS(node.right)
            else:
                return DFS(node.left) and DFS(node.right)
            
        return DFS(root)