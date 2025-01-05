class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        A = ord('a')
        def shiftLetter(ch, amount):
            return chr(((ord(ch) - A + amount) % 26) + A)

        n = len(s)
        diff = [0] * n

        for start, end, direction in shifts:
            diff[start] += 1 if direction else -1
            if end + 1 < n:
                diff[end+1] += -1 if direction else 1

        amount = 0
        ans = list(s)
        for i in range(n):
            amount += diff[i] % 26
            ans[i] = shiftLetter(s[i], amount)

        return "".join(ans)