class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n

        for i in range(1, n):
            if nums[i] % 2 == nums[i-1] % 2:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]

        ans = []
        for start, end in queries:
            ans.append((prefix[end] - prefix[start]) == 0)

        return ans