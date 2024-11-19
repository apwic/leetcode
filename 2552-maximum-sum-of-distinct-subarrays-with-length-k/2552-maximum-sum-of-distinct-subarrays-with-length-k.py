class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {num: i for i, num in enumerate(nums[:k])}
        window = sum(nums[:k])
        ans = 0

        if len(freq) == k:
            ans = window

        for i in range(k, n):
            window += nums[i] - nums[i-k]
            freq[nums[i]] = i

            if freq[nums[i-k]] == i-k:
                del freq[nums[i-k]]
            
            if len(freq) == k:
                ans = max(ans, window)

        return ans
