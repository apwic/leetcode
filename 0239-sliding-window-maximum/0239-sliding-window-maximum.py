class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        stack = deque()
        ans = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            stack.append(i)
            if i >= k-1:
                while stack[0] <= i-k:
                    stack.popleft()
                ans.append(nums[stack[0]])

        return ans

            
            