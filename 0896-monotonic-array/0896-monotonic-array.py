class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if (n == 1):
            return True
        
        a = nums[0]
        b = nums[-1]
        i = 1
        j = n - i - 1
        inc = True
        dec = True
        
        while (i < n):
            if (a > nums[i]):
                inc = False
                
            if (b > nums[j]):
                dec = False
                
            if (not (inc or dec)):
                return False
              
            a = nums[i]
            b = nums[j]
            i += 1
            j = n - i - 1
            
        return inc or dec
        