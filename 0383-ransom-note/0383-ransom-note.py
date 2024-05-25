class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        freq = defaultdict(int)

        for ch in magazine:
            freq[ch] += 1

        for ch in ransomNote:
            if freq[ch]:
                freq[ch] -= 1
            else:
                return False

        return True