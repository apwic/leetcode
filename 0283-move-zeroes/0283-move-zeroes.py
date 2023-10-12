class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums) - 1
        
        while (i < n):
            if (nums[i] == 0):
                nums.append(nums.pop(i))
                n -= 1
            else:
                i += 1
        