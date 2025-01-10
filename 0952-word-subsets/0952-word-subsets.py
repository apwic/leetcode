class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_freq = defaultdict(int)
        for word in words2:
            word_freq = Counter(word)
            for key, val in word_freq.items():
                word2_freq[key] = max(word2_freq[key], val)

        n = len(word2_freq)
        ans = []
        for word in words1:
            word_freq = Counter(word)
            check = 0
            for key, val in word2_freq.items():
                if key not in word_freq:
                    break

                if word2_freq[key] > word_freq[key]:
                    break

                check += 1

            if check == n:
                ans.append(word)

        return ans