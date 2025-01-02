class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(['a', 'i', 'u', 'e', 'o'])
        def checkVowel(word):
            return word[0] in vowel and word[-1] in vowel

        n_w = len(words)
        n_q = len(queries)
        # index 0 as offset
        prefix = [0] * (n_w+1)
        for i in range(1, n_w+1):
            prefix[i] = prefix[i-1] + (1 if checkVowel(words[i-1]) else 0)

        ans = []
        for i, j in queries:
            ans.append(prefix[j+1] - prefix[i])

        return ans