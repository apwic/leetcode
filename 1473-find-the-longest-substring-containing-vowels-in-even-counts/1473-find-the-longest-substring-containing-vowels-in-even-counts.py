class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0,'i': 1, 'u':2, 'e':3, 'o':4}
        bitmask = 0
        freq = {0: -1}

        ans = 0
        for i, char in enumerate(s):
            if char in vowels:
                bitmask ^= (1 << vowels[char])

            if bitmask in freq:
                ans = max(ans, i - freq[bitmask])
            else:
                freq[bitmask] = i

        return ans