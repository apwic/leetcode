class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        n = len(arr)
        half = n//2

        for num in arr:
            freq[num] += 1

        nums = [(val, key) for key, val in freq.items()]
        nums = sorted(nums, key=lambda x: x[0], reverse=True)
        ans = 0

        for val, key in nums:
            n -= val
            ans += 1

            if half >= n:
                return ans
        
        return ans