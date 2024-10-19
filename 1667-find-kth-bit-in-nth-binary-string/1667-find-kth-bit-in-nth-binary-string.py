class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for i in range(n):
            mask = int("1" * len(s), 2)
            s = s + "1" + bin(mask ^ int(s, 2))[2:][::-1]

        return s[k-1]