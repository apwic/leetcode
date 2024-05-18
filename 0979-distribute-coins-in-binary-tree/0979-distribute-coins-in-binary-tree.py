# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def DFS(node):
            if node == None:
                return 0
            
            l = DFS(node.left)
            r = DFS(node.right)
            
            self.moves += abs(l) + abs(r)
            
            return node.val - 1 + l + r
        
        DFS(root)
        return self.moves