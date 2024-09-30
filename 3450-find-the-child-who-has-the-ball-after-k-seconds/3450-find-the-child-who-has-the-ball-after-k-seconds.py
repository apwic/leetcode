class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = (n-1) * 2
        k = k % cycle

        if k < n-1:
            return k + 1 - 1
        else:
            return n - (k - (n-1)) - 1