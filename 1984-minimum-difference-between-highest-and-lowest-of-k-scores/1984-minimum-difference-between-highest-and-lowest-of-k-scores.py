class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        # sort to make it easier
        # window iteration
        nums.sort()
        n = len(nums)

        # 1 4 7 9, k = 3
        # 3 3 2

        # 1 2 2 2 6 10, k = 3
        # 1 0 0 4 4

        ans = nums[-1] - nums[0]
        for i in range(0, n-k+1):
            if nums[i+k-1] - nums[i] < ans:
                ans = nums[i+k-1] - nums[i]

        return ans
