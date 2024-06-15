# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = deque([root])
        depth = 0
        
        while queue:
            curr_len = len(queue)
            arr = [node.val for node in queue]
            # alternate traversal
            if depth % 2 == 1:
                arr.reverse()
            ans.append(arr)

            for _ in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return ans

            