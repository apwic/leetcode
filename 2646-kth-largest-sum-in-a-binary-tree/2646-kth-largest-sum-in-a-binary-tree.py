# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        result = []

        while queue:
            n = len(queue)
            curr_sum = 0
            for i in range(n):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(curr_sum)

        if k > len(result):
            return -1
        
        result.sort()
        return result[-k]
