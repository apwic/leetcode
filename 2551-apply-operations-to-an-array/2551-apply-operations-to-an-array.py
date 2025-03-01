class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        offset = 0
        for i in range(n):
            if i + 1 < n and nums[i] != 0 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

            if nums[i] != 0 and i != offset:
                nums[offset], nums[i] = nums[i], 0
                offset += 1
            elif nums[i] != 0:
                offset += 1

        return nums