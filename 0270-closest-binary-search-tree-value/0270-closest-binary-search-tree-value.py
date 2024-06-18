# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root.left:
            left_val = self.closestValue(root.left, target)
            left_diff = abs(left_val - target)
        
        curr_diff = abs(root.val - target)
        val = root.val

        if root.left and left_diff < curr_diff:
            curr_diff = left_diff
            val = left_val
        if root.left and left_diff == curr_diff:
            val = min(val, left_val)

        if root.right:
            right_val = self.closestValue(root.right, target)
            right_diff = abs(right_val - target)
            if right_diff < curr_diff:
                curr_diff = right_diff
                val = right_val
            if right_diff == curr_diff:
                val = min(val, right_val)

        return val
        