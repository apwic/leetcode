class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))

        def createPrefix(word):
            prefixes = []
            prefix = ""
            for ch in word:
                prefix += ch
                prefixes.append(prefix)

            return prefixes

        freq = defaultdict(int)

        for word in arr1:
            prefixes = createPrefix(word)
            for prefix in prefixes:
                freq[prefix] = 1

        ans = 0

        for word in arr2:
            prefixes = createPrefix(word)
            for prefix in prefixes:
                if prefix in freq:
                    ans = max(ans, len(prefix))

        return ans