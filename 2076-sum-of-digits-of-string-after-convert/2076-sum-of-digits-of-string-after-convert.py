class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''

        for ch in s:
            nums += str(ord(ch) - ord('a') + 1)

        for _ in range(k):
            curr = 0
            for digit in nums:
                curr += int(digit)
            nums = str(curr)

        return int(nums)