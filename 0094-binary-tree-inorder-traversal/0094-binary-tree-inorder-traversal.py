# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []

        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
            
            return self.arr

        return dfs(root)
