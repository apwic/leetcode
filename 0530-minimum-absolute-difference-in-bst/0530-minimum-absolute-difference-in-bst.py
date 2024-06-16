# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, arr=[]):
            if node == None:
                return arr

            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

            return arr

        arr = dfs(root)
        print(arr)
        ans = abs(arr[0] - arr[1]) 
        for i in range(1, len(arr)-1):
            ans = min(ans, abs(arr[i] - arr[i+1]))

        return ans
        