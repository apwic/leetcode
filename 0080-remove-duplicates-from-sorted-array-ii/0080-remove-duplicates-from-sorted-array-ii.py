class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        i, n = 1, len(nums) - 1
        twice = False
        
        while (i <= n):
            a, b = nums[i-1], nums[i]
            if (a != b):
                unique += 1
                i += 1
                twice = False
                
            elif (a == b and not twice):
                unique += 1
                twice = True
                i += 1
            
            elif (a == b and twice):
                nums.append(nums.pop(i))
                n -= 1
                
        return unique
                
                