class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        n = len(nums) - 1
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
            
        ans = 0
        for i in range(n):
            a = prefix[i]
            b = prefix[n] - prefix[i]
            
            if (a >= b):
                ans += 1
            
        return ans