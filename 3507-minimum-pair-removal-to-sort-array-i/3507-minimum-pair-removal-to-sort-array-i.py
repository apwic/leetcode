class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        i, j = 0, 1
        n = len(nums)
        while j < n:
            # find the index where it stops non-decreasing
            while j < n and nums[i] <= nums[j] :
                i += 1
                j += 1

            if j >= n:
                break

            # find min sum
            curr_i, curr_j = i, j
            min_sum = nums[i] + nums[j]
            min_i, min_j = i, j
            while curr_j < n:
                if nums[curr_i] + nums[curr_j] < min_sum:
                    min_sum = nums[curr_i] + nums[curr_j] 
                    min_i, min_j = curr_i, curr_j
                curr_i += 1
                curr_j += 1

            # remove pair and add sum
            nums.pop(min_j)
            nums[min_i] = min_sum
            n = len(nums)
            ans += 1
            i, j = 0, 1

        return ans