class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        
        for i in range(k):
            curr += nums[i]
            
        curr /= k
        sm = curr
        
        for i in range(k, len(nums)):
            curr += nums[i]/k - nums[i-k]/k
            sm = max(sm, curr)
            
        return sm