class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lowerPairs(bound):
            count = 0
            l, r = 0, n-1
            while l < r:
                # needs to be exclusive so that
                # the works for upper + 1
                if nums[l] + nums[r] >= bound:
                    r -= 1
                    continue

                count += r - l
                l += 1

            return count

        n = len(nums)
        nums.sort()

        return lowerPairs(upper+1) - lowerPairs(lower)