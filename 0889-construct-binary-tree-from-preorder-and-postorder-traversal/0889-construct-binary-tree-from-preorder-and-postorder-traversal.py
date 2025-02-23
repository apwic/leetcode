# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        self.j = 0

        def construct():
            root = TreeNode(val = preorder[self.i])
            self.i += 1

            if root.val != postorder[self.j]:
                root.left = construct()

            if root.val != postorder[self.j]:
                root.right = construct()

            self.j += 1
            return root

        return construct()