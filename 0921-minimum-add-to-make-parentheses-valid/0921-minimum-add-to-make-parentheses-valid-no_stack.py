class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        size = 0
        closing = 0
        for ch in s:
            if ch == "(":
                size += 1
            else:
                if size > 0:
                    size -= 1
                else:
                    closing += 1

        return size + closing