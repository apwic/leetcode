class Solution:
    def clearDigits(self, s: str) -> str:
        numeric = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        stack = []
        for ch in s:
            if ch not in numeric:
                stack.append(ch)
                continue

            if stack:
                stack.pop()

        return "".join(stack)