class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        freq = defaultdict(int)

        for ch in s1:
            freq[ch] += 1

        def checkFreq(s, freq):
            for ch in s:
                if freq[ch]:
                    freq[ch] -= 1

            return sum([freq[ch] for ch in s1]) == 0

        for i in range(n2-n1+1):
            if checkFreq(s2[i:i+n1], freq.copy()):
                return True

        return False
