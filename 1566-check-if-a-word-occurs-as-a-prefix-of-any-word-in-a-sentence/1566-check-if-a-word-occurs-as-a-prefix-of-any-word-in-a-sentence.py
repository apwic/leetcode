class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        freq = defaultdict(int)

        for i, word in enumerate(sentence.split(' ')):
            for j in range(len(word)):
                if freq[word[:j+1]]:
                    continue

                freq[word[:j+1]] = i+1

        if freq[searchWord]:
            return freq[searchWord]

        return -1