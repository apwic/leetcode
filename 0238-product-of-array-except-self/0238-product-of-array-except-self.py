class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]

        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        ans = [1] * n
        for i in range(n):
            if i == 0:
                ans[i] = suffix[i+1]
            elif i == n-1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = prefix[i-1] * suffix[i+1]

        return ans