class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        found = False
        x = 1
        
        while not found:
            prefix = [x]
            
            for i in range(len(nums)):
                a = prefix[i]
                b = nums[i]
                if (a + b < 1):
                    x += 1
                    break
                else:
                    prefix.append(a + b)
                    
            if (len(prefix) == len(nums) + 1):
                found = True
                
        return x