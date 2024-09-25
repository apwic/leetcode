class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                node.suggestions.append(product)
                node.suggestions.sort()

                if len(node.suggestions) > 3:
                    node.suggestions.pop()

        ans = []
        node = root
        for ch in searchWord:
            if ch in node.children:
                node = node.children[ch]
                ans.append(node.suggestions)
            else:
                node.children = {}
                ans.append([])

        return ans