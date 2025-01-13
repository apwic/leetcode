class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for val in freq.values():
            if val % 2 == 0:
                ans += 2
            else:
                ans += 1

        return ans