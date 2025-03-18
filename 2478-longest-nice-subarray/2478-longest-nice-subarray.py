class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        ans = 1
        for r in range(1, n):
            check = True
            i = l
            while i < r:
                if nums[i] & nums[r] == 0:
                    i += 1
                else:
                    l += 1
                    i = l
            
            ans = max(ans, r-l+1)

        return ans