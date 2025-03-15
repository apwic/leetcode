class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1, max(nums)
        n = len(nums)

        while l < r:
            mid = (l + r) // 2
            possible = 0

            i = 0
            while i < n:
                if nums[i] <= mid:
                    possible += 1
                    i += 2
                else:
                    i += 1

            if possible >= k:
                r = mid
            else:
                l = mid + 1

        return l