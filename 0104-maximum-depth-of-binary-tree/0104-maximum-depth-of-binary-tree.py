# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth=0):
            if node == None:
                return depth
            
            depth_l = dfs(node.left, depth+1)
            depth_r = dfs(node.right, depth+1)

            return max(depth_l,depth_r)

        return dfs(root)
