class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sums = sum(nums)
        rem = sums % p

        if rem == 0:
            return 0

        freq = {0: -1}
        prefix = 0
        ans = n

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - rem + p) % p
            
            if target in freq:
                ans = min(ans, i - freq[target])

            freq[prefix] = i

        return ans if ans != n else -1