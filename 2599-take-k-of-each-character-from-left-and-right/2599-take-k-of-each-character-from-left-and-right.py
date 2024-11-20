class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        freq = Counter(s)

        if freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1

        ans = n
        l = 0
        for r in range(n):
            freq[s[r]] -= 1

            while l <= r and (freq['a'] < k or freq['b'] < k or freq['c'] < k):
                freq[s[l]] += 1
                l += 1

            ans = min(ans, freq['a'] + freq['b'] + freq['c'])
            
        return ans