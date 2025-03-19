class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if sum(nums) == n:
            return 0

        ans = 0
        for i in range(n-2):
            if nums[i] == 0:
                for i in range(i, i+3):
                    nums[i] ^= 1
                ans += 1

        if sum(nums) != n:
            return -1

        return ans