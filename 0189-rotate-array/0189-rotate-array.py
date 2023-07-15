class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        k = len(nums) - k
        
        temp = nums[k:] + nums[:k]
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
            
