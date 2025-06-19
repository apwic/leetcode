class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_min, curr_max = nums[0], nums[0]
        ans = 1

        for num in nums:
            curr_max = num

            if curr_max - curr_min > k:
                curr_min, curr_max = num, num
                ans += 1

        return ans
        