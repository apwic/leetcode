# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(node, p):
            if p == None:
                return True

            if node == None:
                return False

            if node.val != p.val:
                return False

            return check(node.left, p.next) or check(node.right, p.next)

        def dfs(node, exist=False):
            if node == None:
                return False

            if node.val == head.val:
                exist = check(node.left, head.next) or check(node.right, head.next)

            if not exist:
                return dfs(node.left) or dfs(node.right)
            else:
                return True

        return dfs(root)