# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graphs = defaultdict(set)

        def dfs(node):
            if node.left:
                graphs[node.val].add(node.left.val)
                graphs[node.left.val].add(node.val)
                dfs(node.left)

            if node.right:
                graphs[node.val].add(node.right.val)
                graphs[node.right.val].add(node.val)
                dfs(node.right)

        dfs(root)
        
        queue = deque([target.val])
        seen = set()
        depth = 0
        ans = []

        while queue:
            curr_len = len(queue)

            for _ in range(curr_len):
                node = queue.popleft()
                if node not in seen:
                    seen.add(node)
                    
                    if depth == k:
                        ans.append(node)

                    for neighbor in graphs[node]:
                        queue.append(neighbor)

            if depth == k:
                return ans

            depth += 1
                
        return ans