class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] != 0 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        offset = 0
        for i in range(n):
            if nums[i] != 0 and i != offset:
                nums[offset], nums[i] = nums[i], 0
                offset += 1
            elif nums[i] != 0:
                offset += 1

        return nums