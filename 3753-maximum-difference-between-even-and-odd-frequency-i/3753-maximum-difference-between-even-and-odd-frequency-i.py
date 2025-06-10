class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        a1 = 0
        a2 = len(s)

        for val in freq.values():
            if val % 2 == 1:
                if val > a1:
                    a1 = val
            else:
                if a2 > val:
                    a2 = val

        return a1 - a2