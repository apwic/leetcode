class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        freq = defaultdict(int)

        for word in s1:
            freq[word] += 1

        for word in s2:
            freq[word] += 1

        ans = []
        for word in freq.keys():
            if freq[word] == 1:
                ans.append(word)

        return ans