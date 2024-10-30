class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        LIS, LDS = [1] * n, [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)

        ans = float('inf')
        for i in range(n):
            if LIS[i] > 1 and LDS[i] > 1:
                ans = min(ans, n - LIS[i] - LDS[i] + 1)

        return ans