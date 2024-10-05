class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def idx(ch):
            return ord(ch) - ord('a')

        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        freq1, freq2 = [0] * 26, [0] * 26

        for i in range(n1):
            freq1[idx(s1[i])] += 1
            freq2[idx(s2[i])] += 1

        if freq1 == freq2:
            return True

        for i in range(n1, n2):
            start = s2[i-n1]
            end = s2[i]

            freq2[idx(start)] -= 1
            freq2[idx(end)] += 1

            if freq1 == freq2:
                return True

        return False
