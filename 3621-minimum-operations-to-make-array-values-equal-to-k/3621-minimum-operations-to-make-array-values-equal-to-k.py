class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        N = 101
        freq = [0] * N
        for num in nums:
            freq[num] += 1

        for num in range(0, k):
            if freq[num] > 0:
                return -1

        ans = 0
        for num in range(k+1, N):
            if freq[num]:
                ans += 1

        return ans