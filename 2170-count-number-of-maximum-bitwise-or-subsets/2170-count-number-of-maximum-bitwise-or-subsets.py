class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        target = 0
        for num in nums:
            target = target | num

        def backtrack(idx=0, curr=0):
            if idx == n:
                return 1 if curr == target else 0

            exclude = backtrack(idx+1, curr)
            include = backtrack(idx+1, curr | nums[idx])

            return exclude + include

        return backtrack()