class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        ans = 0

        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        for j in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack.pop())

        return ans