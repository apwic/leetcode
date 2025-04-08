class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        while len(set(nums)) != len(nums):
            nums = nums[(min(3, len(nums))):]
            ans += 1

        return ans