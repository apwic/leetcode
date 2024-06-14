# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node, depth):
            if node == None:
                return depth

            left = dfs(node.left, depth)
            right = dfs(node.right, depth)
            
            self.diameter = max(left+right, self.diameter)

            return max(left, right) + 1

        dfs(root, 0)
        return self.diameter
        