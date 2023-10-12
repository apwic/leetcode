class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if (k == 0):
            return nums
        
        n = len(nums)
        
        if (k >= n):
            return [-1 for i in range(n)]
        
        prefix = [nums[0]]     
        for i in range(1, n):
            prefix.append(prefix[i-1] + nums[i])
        
        ans = []
        z = 2*k + 1
        for i in range(n):
            if (i - k < 0 or i + k > n - 1):
                ans.append(-1)
            else:
                a, b = prefix[i - k], prefix[i + k]
                c = nums[i - k]
                    
                ans.append((b-a+c)//z)
                
        return ans