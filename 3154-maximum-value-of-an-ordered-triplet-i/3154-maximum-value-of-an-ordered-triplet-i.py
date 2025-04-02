class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] - nums[j] < 0:
                    continue

                for k in range(j+1, n):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])

        return ans if ans > 0 else 0