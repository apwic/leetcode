class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        index = {}

        for i in range(n):
            ch = s[i]
            if ch in index:
                index[ch] = max(index[ch], i)
            else:
                index[ch] = i

        ans = []
        min_idx, max_idx = 0, index[s[0]]
        for i in range(n):
            if i == max_idx:
                ans.append(max_idx - min_idx + 1)

                if i+1 < n:
                    min_idx, max_idx = i+1, index[s[i+1]]
            else:
                max_idx = max(max_idx, index[s[i]])

        return ans