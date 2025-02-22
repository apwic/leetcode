# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def DFS(node, depth, i):
            # LEFT
            local_depth = 0
            while i + local_depth < n and traversal[i + local_depth] == "-":
                local_depth += 1

            if local_depth == depth:
                i += depth

                num = []
                # find until all number is clear
                while i < n and traversal[i] != "-":
                    num.append(traversal[i])
                    i += 1

                num = int("".join(num))
                
                node.left = TreeNode(val=num)
                i = DFS(node.left, depth+1, i)
            else:
                return i

            # RIGHT
            local_depth = 0
            while i + local_depth < n and traversal[i + local_depth] == "-":
                local_depth += 1

            if local_depth == depth:
                i += depth

                num = []
                # find until all number is clear
                while i < n and traversal[i] != "-":
                    num.append(traversal[i])
                    i += 1

                num = int("".join(num))

                node.right = TreeNode(val=num)
                i = DFS(node.right, depth+1, i)
            else:
                return i

            return i 
            
        n = len(traversal)
        num = []
        # find until all number is clear
        i = 0
        while i < n and traversal[i] != "-":
            num.append(traversal[i])
            i += 1

        num = int("".join(num))
        root = TreeNode(val=num)

        DFS(root, 1, i)
        return root