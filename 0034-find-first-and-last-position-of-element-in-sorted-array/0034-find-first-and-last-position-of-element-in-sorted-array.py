class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findStart():
            l, r = 0, len(nums) - 1
            while (l <= r):
                m = l + (r-l)//2
                if (target <= nums[m]):
                    r = m - 1
                else:
                    l = m + 1
                    
            return l
         
        def findEnd():
            l, r = 0, len(nums) - 1
            while (l <= r):
                m = l + (r-l)//2
                if (nums[m] <= target):
                    l = m + 1
                else:
                    r = m - 1
                    
            return r
        
        s, e = findStart(), findEnd()
        print(s, e)
        
        if (s <= e):
            return [s, e]
        else:
            return [-1, -1]
                
            