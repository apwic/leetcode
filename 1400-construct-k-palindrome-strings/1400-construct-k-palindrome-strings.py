class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True

        freq = Counter(s)
        even = odd = 0
        for val in freq.values():
            even += val // 2
            odd += val % 2

        return not odd > k
