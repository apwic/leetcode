class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        n -= 1
        mask = 1

        while n > 0:
            # check bit position to toggle the bit
            if (x & mask) == 0:
                # check if LSB of n == 1
                # LSB of n determine this toggle
                if (n & 1) == 1:
                    ans |= mask
                n >>= 1
            mask <<= 1

        return ans

            