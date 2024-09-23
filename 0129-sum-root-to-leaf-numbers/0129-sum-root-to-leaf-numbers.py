# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def DFS(node=root, curr="", arr=[]):
            if node == None:
                return arr

            curr += str(node.val)

            DFS(node.left, curr, arr)
            DFS(node.right, curr, arr)

            if not (node.left or node.right):
                arr.append(curr)

            return arr

        return sum(list(map(int, DFS())))