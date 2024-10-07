class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if (len(stack) > 0) and ((stack[-1] == "A" and ch == "B") or (stack[-1] == "C" and ch == "D")):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)