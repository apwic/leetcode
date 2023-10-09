class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if (k <= 1):
            return 0
        
        l = 0
        count = 0
        curr = 1
        
        for r in range(len(nums)):
            curr *= nums[r]
            
            while (curr >= k):
                curr //= nums[l]
                l += 1
                
            count += r - l + 1
            
        return count