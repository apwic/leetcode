class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freqA = defaultdict(bool)
        freqB = defaultdict(bool)
        prefix = [0]

        for i in range(n):
            freqA[A[i]] = True
            freqB[B[i]] = True

            if A[i] == B[i]:
                prefix.append(prefix[-1] + 1)
                continue

            curr = 0
            if freqB[A[i]]:
                curr += 1

            if freqA[B[i]]:
                curr += 1

            prefix.append(prefix[-1] + curr)

        return prefix[1:]
            