# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = []
        queue = deque([root])
        while queue:
            size = len(queue)
            curr_sum = 0
            for _ in range(size):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            sums.append(curr_sum)

        def dfs(node, depth, sibling=0):
            if node == None:
                return

            if depth == 0 or depth == 1:
                node.val = 0
            else:
                node.val = sums[depth] - sibling

            sibling_sum = 0
            if node.left:
                sibling_sum += node.left.val
            if node.right:
                sibling_sum += node.right.val

            dfs(node.left, depth + 1, sibling_sum)
            dfs(node.right, depth + 1, sibling_sum)

        dfs(root, 0)
        return root