class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # must get first element
        ans = nums[0]

        # then we can just find two minimum element
        ans += sum(sorted(nums[1:])[:2])

        return ans