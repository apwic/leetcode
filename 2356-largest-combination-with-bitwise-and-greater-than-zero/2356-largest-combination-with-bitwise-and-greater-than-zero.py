class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        freq = defaultdict(int)

        for num in candidates:
            i = 0
            while num:
                if num & 1:
                    freq[i] += 1
                num = num >> 1
                i += 1

        return max(freq.values())