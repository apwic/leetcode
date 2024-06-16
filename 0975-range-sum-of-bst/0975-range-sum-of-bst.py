# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            if low <= node.val <= high:
                self.ans += node.val
            dfs(node.right)

        dfs(root)
        return self.ans
        