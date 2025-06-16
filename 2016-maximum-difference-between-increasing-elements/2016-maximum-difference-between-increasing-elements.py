class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        stack = []
        ans = -1
        
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()

            stack.append(num)

            if stack[0] != stack[-1]:
                ans = max(ans, stack[-1] - stack[0])

        return ans