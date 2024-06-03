class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            # abs diff betwen lower and upper letter in ascii
            # = 32 
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack) 
