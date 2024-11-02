class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        n = len(sentence)
        first = sentence[0][0]
        last = sentence[0][-1]

        for idx in range(1, n):
            last = sentence[idx][-1]
            if sentence[idx-1][-1] != sentence[idx][0]:
                return False

        return first == last