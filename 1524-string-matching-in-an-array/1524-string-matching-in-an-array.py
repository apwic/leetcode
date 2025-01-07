class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        freq = defaultdict(bool)

        for word in words:
            n = len(word)
            for i in range(n):
                substr = []
                for j in range(i, n):
                    substr.append(word[j])
                    joined = "".join(substr)
                    if joined != word:
                        freq["".join(substr)] = True
                        
        ans = []
        for word in words:
            if freq[word]:
                ans.append(word)

        return ans