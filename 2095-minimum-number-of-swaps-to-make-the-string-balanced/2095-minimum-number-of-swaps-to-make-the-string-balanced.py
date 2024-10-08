class Solution:
    def minSwaps(self, s: str) -> int:
        size = 0

        for ch in s:
            if ch == "[":
                size += 1
            else:
                if size > 0:
                    size -= 1

        return ceil(size / 2)