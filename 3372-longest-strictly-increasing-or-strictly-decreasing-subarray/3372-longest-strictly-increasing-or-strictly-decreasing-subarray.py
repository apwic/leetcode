class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = [], []
        ans = 0

        for num in nums:
            if inc and inc[-1] >= num:
                inc = []
            inc.append(num)

            if dec and dec[-1] <= num:
                dec = []
            dec.append(num)

            ans = max(ans, len(inc), len(dec))

        return ans
