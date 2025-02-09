class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff = defaultdict(int)

        for i in range(n):
            diff[nums[i] - i] += 1

        ans = n*(n-1)//2
        for val in diff.values():
            if val <= 1:
                continue

            ans -= val*(val-1)//2

        return ans
