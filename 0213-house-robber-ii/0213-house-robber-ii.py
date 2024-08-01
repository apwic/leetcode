class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp1 = [0] * (n)
        dp2 = [0] * (n)

        for i in range(n):
            two_prev, prev = (i-2)%n, (i-1)%n
            # 1st case: include first and exclude last (0 to n-1)
            if i < n-1:
                dp1[i] = max(dp1[two_prev] + nums[i], dp1[prev])

            # 2nc case: exclue first and include last (1 to n)
            if i > 0:
                dp2[i] = max(dp2[two_prev] + nums[i], dp2[prev])

        return max(max(dp1), max(dp2))