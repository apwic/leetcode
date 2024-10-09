class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in s:
            if len(stack) > 0 and (stack[-1] == "(" and ch == ")"):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)