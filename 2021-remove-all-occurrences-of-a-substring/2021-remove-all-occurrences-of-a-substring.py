class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        p = len(part)

        for ch in s:
            stack.append(ch)
            if "".join(stack[-p:]) == part:
                del stack[-p:]

        return "".join(stack)