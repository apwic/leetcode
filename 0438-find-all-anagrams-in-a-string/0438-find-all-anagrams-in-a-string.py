class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def idx(ch):
            return ord(ch) - ord('a')

        n_p, n_s = len(p), len(s)

        if n_p > n_s:
            return []
            
        freq_p, freq_s = [0] * 26, [0] * 26
        
        for i in range(n_p):
            freq_p[idx(p[i])] += 1
            freq_s[idx(s[i])] += 1

        ans = []
        if freq_p == freq_s:
            ans.append(0)

        for i in range(n_p, n_s):
            start = s[i - n_p]
            end = s[i]

            freq_s[idx(start)] -= 1
            freq_s[idx(end)] += 1

            if freq_p == freq_s:
                ans.append(i - n_p + 1)

        return ans