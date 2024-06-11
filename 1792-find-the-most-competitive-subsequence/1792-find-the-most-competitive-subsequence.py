class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []

        for i in range(len(nums)):
            rem = len(nums) - i
            # need to check if there's enough remaining element
            # for stack to be popped
            while stack and stack[-1] > nums[i] and len(stack) - 1 + rem >= k:
                stack.pop()

            if len(stack) < k:
                stack.append(nums[i])

        return stack