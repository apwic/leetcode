class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0

        for num in nums:
            curr = num
            curr_len = 0

            while curr in set_nums:
                curr_len += 1

                temp = curr * curr
                if temp > 10**5:
                    break

                curr = temp

            ans = max(ans, curr_len)

        return ans if ans >= 2 else -1