class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        mn = n + 1
        l = curr = 0
        for r in range(n):
            curr += nums[r]
            
            while curr >= target:
                mn = min(mn, r - l + 1)
                curr -= nums[l]
                l += 1
                
        return mn if mn <= n else 0
                
            