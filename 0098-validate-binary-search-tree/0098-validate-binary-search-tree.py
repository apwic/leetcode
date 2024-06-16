# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, arr=[]):
            if node == None:
                return arr

            dfs(node.left,arr)
            arr.append(node.val)
            dfs(node.right,arr)

            return arr

        arr = dfs(root)
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                return False

        return True


