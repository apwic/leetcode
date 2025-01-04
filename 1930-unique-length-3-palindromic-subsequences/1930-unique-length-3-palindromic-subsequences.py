class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first, last = [-1] * 26, [-1] * 26

        for i in range(n):
            ord_ch = ord(s[i]) - ord('a')
            if first[ord_ch] == -1:
                first[ord_ch] = i

            last[ord_ch] = i

        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue

            ans += len(set(s[first[i]+1:last[i]]))

        return ans