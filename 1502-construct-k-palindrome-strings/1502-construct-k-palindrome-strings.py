class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True

        freq = Counter(s)
        odd = 0
        for val in freq.values():
            odd += val % 2

        return odd <= k
