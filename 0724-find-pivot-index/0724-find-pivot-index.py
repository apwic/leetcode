class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
        
        for i in range(1, n):
            prefix.append(prefix[i-1] + nums[i])
            
        for i in range(n):
            if (i == 0):
                l = 0
            else:
                l = prefix[i-1]
                
            if (i == n - 1):
                r = 0
            else:
                r = prefix[-1] - prefix[i+1] + nums[i+1]
            
            if (l == r):
                return i
            
        return -1