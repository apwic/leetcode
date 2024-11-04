class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        before = word[0]
        count = 1

        for ch in word[1:]:
            if before != ch:
                ans.append(str(count) + before)
                count = 1
                before = ch
                continue

            if count >= 9:
                ans.append("9" + before)
                count = 1
            else:
                count += 1

        ans.append(str(count) + before)
        return ''.join(ans)