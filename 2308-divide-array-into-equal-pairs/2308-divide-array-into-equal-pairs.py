class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for val in freq.values():
            if val % 2 == 1:
                return False

        return True