class Solution:
    def bitwiseComplement(self, n: int) -> int:
        len_n = len(bin(n)) - 2
        mask = (1 << len_n) - 1
        return n ^ mask