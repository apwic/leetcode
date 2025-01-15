class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        sb1, sb2 = num1.bit_count(), num2.bit_count()

        ans = 0
        for i in range(31, -1, -1):
            if sb2 > 0 and (num1 & (1 << i)):
                ans |= (1 << i)
                sb2 -= 1

        for i in range(32):
            if sb2 > 0 and not (ans & (1 << i)):
                ans |= (1 << i)
                sb2 -= 1

        return ans
