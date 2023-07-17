class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            mx = 0
            for k in range(i):
                if (mx < LIS[k] and nums[k] < nums[i]):
                    mx = LIS[k]
            LIS[i] = 1 + mx
                    
        return max(LIS)
                
                
        