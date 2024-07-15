class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            sums = 0
            for num in nums:
                sums += math.ceil(num / divisor)

            return sums <= threshold

        l, r = 1, sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
