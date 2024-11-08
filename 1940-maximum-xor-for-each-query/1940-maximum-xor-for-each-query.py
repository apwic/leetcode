class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_bit = (1 << maximumBit) - 1

        prefix = 0
        for num in nums:
            prefix ^= num

        ans = [0] * n
        suffix = 0
        for i in range(n):
            ans[i] = prefix ^ suffix ^ max_bit
            suffix ^= nums[n-1-i]

        return ans
