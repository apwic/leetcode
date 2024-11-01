class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = [s[0]]
        curr = s[0]
        count = 1
        for idx, ch in enumerate(s[1:]):
            if ch == curr:
                if count >= 2:
                    continue
                count += 1
            else:
                curr = ch
                count = 1

            ans.append(ch)

        return ''.join(ans)