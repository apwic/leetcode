class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i in range(len(nums)):
            num = nums[i]
            cmp = target - num
            
            if (hm.get(cmp) != None):
                return [i, hm[cmp]]
        
            hm[num] = i
            
        return [-1, -1]
                
                