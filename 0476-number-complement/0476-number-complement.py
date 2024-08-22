class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num)) - 2
        mask = int('1' * n, 2)
        return mask^num