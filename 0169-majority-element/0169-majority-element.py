class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = 10**9 + 1
        
        for i in range(len(nums)):
            if (count == 0):
                cand = nums[i]
                count = 1
            else:
                if (cand == nums[i]):
                    count += 1
                else:
                    count -= 1
                    
        return cand