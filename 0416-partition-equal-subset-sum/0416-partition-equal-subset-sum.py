class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        @lru_cache(maxsize=None)
        def backtrack(curr, idx):
            if target == curr:
                return True

            if idx == n:
                return False

            return backtrack(curr, idx+1) or  backtrack(curr+nums[idx], idx + 1)

        return backtrack(0, 0)