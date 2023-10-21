from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hm = defaultdict(int)
        
        for l in nums:
            for x in l:
                hm[x] += 1
                
        n = len(nums)
        ans = []
        
        for i in hm:
            if hm[i] == n:
                ans.append(i)
                
        return sorted(ans)