# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_val):
            if node == None:
                return 0

            if node.val >= max_val:
                self.count += 1

            max_val = max(max_val, node.val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

        dfs(root, root.val)
        return self.count
        