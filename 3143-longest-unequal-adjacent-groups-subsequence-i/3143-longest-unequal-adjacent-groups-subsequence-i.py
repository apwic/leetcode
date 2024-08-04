class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        last_idx_0, last_idx_1 = -100, -100
        idx_0, idx_1 = [], []

        for i in range(n):
            if groups[i] == 0:
                if last_idx_0 != i-1:
                    idx_0 = idx_1 + [i]
                last_idx_0 = i
            else:
                if last_idx_1 != i-1:
                    idx_1 = idx_0 + [i]
                last_idx_1 = i

        idx = idx_0 if len(idx_0) > len(idx_1) else idx_1
        ans = []

        for i in idx:
            ans.append(words[i]) 

        return ans