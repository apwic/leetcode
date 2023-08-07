class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def findCircular(nums, idx):
            n = len(nums)
            mx = nums[idx]
            for i in range(idx, idx + n):
                if (mx < nums[i % n]):
                    return nums[i % n]
                    
            return - 1        

        ret = []
        for i in range(len(nums)):
            ret.append(findCircular(nums, i))
            
        return ret
                    
            
        
            
        