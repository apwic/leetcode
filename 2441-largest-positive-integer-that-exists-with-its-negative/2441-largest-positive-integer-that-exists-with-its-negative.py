class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1 
        
        for num in nums:
            if -1 * num not in nums:
                continue
                
            if num > ans:
                ans = num
                
        return ans