class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if len(stack) > 0  \
                and ((stack[-1] == "(" and ch == ")") \
                or (stack[-1] == "{" and ch == "}") \
                or (stack[-1] == "[" and ch == "]")):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
