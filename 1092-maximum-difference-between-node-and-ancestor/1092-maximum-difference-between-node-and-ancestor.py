# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_val, max_val):
            if node == None:
                return 0

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            diff = abs(max_val - min_val)

            left = dfs(node.left, min_val, max_val)
            right = dfs(node.right, min_val, max_val)

            return max(diff, left, right)
        
        return dfs(root, root.val, root.val)