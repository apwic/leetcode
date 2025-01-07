class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_set = set(words)
        ans = set([])

        for word in words:
            n = len(word)
            for i in range(n):
                substr = []
                for j in range(i, n):
                    substr.append(word[j])
                    joined = "".join(substr)
                    if joined != word and joined in words_set:
                        ans.add(joined)

        return list(ans)