class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start ^ goal
        val = {'0': 0, '1': 1}
        ans = 0

        for digit in bin(num)[2:]:
            ans += val[digit]

        return ans