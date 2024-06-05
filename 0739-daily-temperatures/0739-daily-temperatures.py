class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pop = stack.pop()
                ans[pop] = i - pop

            stack.append(i)

        return ans 
        