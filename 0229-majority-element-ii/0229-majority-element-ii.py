class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, p1, p2 = 0, 0, None, None
        n = len(nums)
        
        for num in nums:
            if (num == p1):
                c1 += 1
            elif (num == p2): 
                c2 += 1
            elif (c1 == 0):
                c1, p1 = 1, num
            elif (c2 == 0):
                c2, p2 = 1, num
            else:
                c1 -= 1
                c2 -= 1
                
        c1, c2 = 0, 0
        for num in nums:
            if (num == p1):
                c1 += 1
            if (num == p2):
                c2 += 1       
            
        res = []
        if c1 > (n//3):
            res.append(p1)
        if c2 > (n//3):
            res.append(p2)
            
            
        return res