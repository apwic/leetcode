class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        freq_s1, freq_s2 = defaultdict(int), defaultdict(int)

        for word in s1:
            freq_s1[word] += 1

        for word in s2:
            freq_s2[word] += 1

        ans = []
        for word in freq_s1.keys():
            if freq_s1[word] == 1 and not freq_s2[word]:
                ans.append(word)

        for word in freq_s2.keys():
            if freq_s2[word] == 1 and not freq_s1[word]:
                ans.append(word)

        return ans