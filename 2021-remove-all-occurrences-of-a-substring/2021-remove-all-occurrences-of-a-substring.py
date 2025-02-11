class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        p = len(part)

        for ch in s:
            stack.append(ch)
            if stack[-p:] == part:
                for _ in range(p):
                    stack.pop()

        return "".join(stack)