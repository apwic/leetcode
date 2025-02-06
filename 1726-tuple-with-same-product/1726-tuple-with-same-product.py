class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)

        for i in range(n):
            for j in range(i+1, n):
                freq[nums[i] * nums[j]] += 1

        ans = 0
        for val in freq.values():
            if val > 1:
                ans += val * (val-1) // 2

        return ans * 8