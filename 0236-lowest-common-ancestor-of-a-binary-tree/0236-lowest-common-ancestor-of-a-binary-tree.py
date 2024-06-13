# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None

        def dfs(node, found_p=False, found_q=False):
            if node == None:
                return False, False
            
            lfp, lfq = dfs(node.left, found_p, found_q)
            rfp, rfq = dfs(node.right, found_p, found_q)

            if node == p or lfp or rfp:
                found_p = True
            
            if node == q or lfq or rfq:
                found_q = True

            if found_p and found_q:
                self.ancestor = node
                return False, False

            return found_p, found_q

        dfs(root)
        return self.ancestor
            
        