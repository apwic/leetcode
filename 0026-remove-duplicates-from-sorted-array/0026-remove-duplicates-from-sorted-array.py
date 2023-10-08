class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        i = 1
        n = len(nums)
        
        while (i < n):
            if (nums[i-1] == nums[i]):
                nums.append(nums.pop(i))
                n -= 1
            else:
                unique += 1
                i += 1
                
        return unique
        