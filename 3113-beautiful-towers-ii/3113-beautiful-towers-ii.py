class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        def calculate(heights):
            stack = []
            prefix = [0] * n
            curr = 0

            for i, height in enumerate(heights):
                count = 1
                while stack and height <= stack[-1][0]:
                    h, c = stack.pop()
                    curr -= h * c
                    count += c

                stack.append((height, count))
                curr += height * count
                prefix[i] = curr

            return prefix

        left = calculate(maxHeights)
        right = calculate(maxHeights[::-1])[::-1]
        
        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] - maxHeights[i])

        return ans