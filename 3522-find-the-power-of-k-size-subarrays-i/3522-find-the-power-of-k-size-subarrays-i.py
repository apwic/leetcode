class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        n = len(nums)
        count = 1
        ans = [-1] * (n-k+1)

        for i in range(n-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                count = 1

            if count >= k:
                ans[i-k+2] = nums[i+1]

        return ans
