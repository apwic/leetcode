class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if len(words[i]) > len(words[j]):
                    continue

                p = len(words[i])
                q = len(words[j])
                prefix = words[i] == words[j][:p] 
                suffix = words[i] == words[j][q-p:]

                if prefix and suffix:
                    ans += 1

        return ans