class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        ZERO = "0"
        OPEN = "("
        CLOSE = ")"

        n = len(s)
        if n % 2 == 1:
            return False

        open_count = []
        zero_count = []

        for i in range(n):
            if locked[i] == ZERO:
                zero_count.append(i)
            elif s[i] == OPEN:
                open_count.append(i)
            elif s[i] == CLOSE:
                # prioritize the open with the close
                if open_count:
                    open_count.pop()
                elif zero_count:
                    zero_count.pop()
                # not matched
                else:
                    return False

        # try matching the open with zero
        while open_count and zero_count and open_count[-1] < zero_count[-1]:
            open_count.pop()
            zero_count.pop()

        # "(" still remaining, it's not matched
        if open_count:
            return False

        return True
