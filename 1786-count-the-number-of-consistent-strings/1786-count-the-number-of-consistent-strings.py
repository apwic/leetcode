class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def checkAllowed(word):
            for ch in word:
                if not freq[ch]:
                    return False

            return True

        freq = defaultdict(int)

        for ch in allowed:
            freq[ch] += 1

        ans = 0
        for word in words:
            ans += 1 if checkAllowed(word) else 0
                
        return ans