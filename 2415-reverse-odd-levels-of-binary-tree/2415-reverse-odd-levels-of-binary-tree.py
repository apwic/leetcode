# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fill(orig, node):
            if orig == None:
                return

            node.val = orig.val
            node.left = TreeNode()
            node.right = TreeNode()

            fill(orig.left, node.left)
            fill(orig.right, node.right)

        inverted = TreeNode()
        fill(root, inverted)

        def invert(node):
            if node == None:
                return

            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(inverted)

        def invertOdd(node, inverted, level):
            if node == None:
                return

            if level % 2 == 0 and node.left and node.right:
                node.left.val = inverted.left.val
                node.right.val = inverted.right.val

            invertOdd(node.left, inverted.left, level+1)
            invertOdd(node.right, inverted.right, level+1)

        invertOdd(root, inverted, 0)

        return root

