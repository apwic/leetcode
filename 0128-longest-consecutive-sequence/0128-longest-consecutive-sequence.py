class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        ans = 0
        for num in nums:
            if num - 1 in nums_set:
                continue

            curr = 1
            next_num = num + 1
            while next_num in nums_set:
                curr += 1
                next_num += 1

            ans = max(ans, curr)

        return ans
