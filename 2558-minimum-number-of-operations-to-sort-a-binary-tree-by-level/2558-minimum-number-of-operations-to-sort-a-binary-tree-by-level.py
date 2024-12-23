# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 0

        while queue:
            level_size = len(queue)
            arr = []

            for i in range(level_size):
                node = queue.popleft()

                if node == None:
                    continue

                arr.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            idx = defaultdict(int)
            sorted_arr = sorted(arr)
            for i, val in enumerate(arr):
                idx[val] = i

            for i in range(len(arr)):
                # index is correct
                if arr[i] == sorted_arr[i]:
                    continue

                # update the idx to the correct val
                target_idx = idx[sorted_arr[i]]
                idx[arr[i]] = target_idx
                arr[target_idx] = arr[i]

                ans += 1

        return ans