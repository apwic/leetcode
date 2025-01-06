class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix = [0] * n
        ball = 1 if boxes[0] == "1" else 0 
        for i in range(1, n):
            prefix[i] = prefix[i-1] + ball
            ball += 1 if boxes[i] == "1" else 0

        suffix = [0] * n
        ball = 1 if boxes[n-1] == "1" else 0 
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + ball
            ball += 1 if boxes[i] == "1" else 0

        ans = [0] * n
        for i in range(n):
            ans[i] = prefix[i] + suffix[i]

        return ans