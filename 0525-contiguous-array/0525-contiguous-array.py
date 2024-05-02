class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        freq = {0 : -1}
        
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            
            if count in freq:
                ans = max(ans, i - freq[count])
            else:
                freq[count] = i
                
        return ans
            