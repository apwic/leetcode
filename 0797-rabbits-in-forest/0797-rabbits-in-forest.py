class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)

        for num in answers:
            freq[num] += 1

        ans = 0
        for key, val in freq.items():
            num = key + 1
            ans += ceil(val/num) * num

        return ans