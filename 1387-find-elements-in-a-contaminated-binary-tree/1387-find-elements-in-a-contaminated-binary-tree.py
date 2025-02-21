# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __fill(self, node):
        if not node:
            return

        if node.left:
            node.left.val = node.val * 2 + 1
            self.freq[node.left.val] = True
            self.__fill(node.left)

        if node.right:
            node.right.val = node.val * 2 + 2
            self.freq[node.right.val] = True
            self.__fill(node.right)
            
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.freq = defaultdict(bool)
        self.freq[0] = True

        self.__fill(self.root)

    def find(self, target: int) -> bool:
        return self.freq[target]

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)