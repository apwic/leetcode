class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = n - 1
        
        for i in range(n-2, -1, -1):
            if (i + nums[i] >= r):
                r = i
                
        return r == 0