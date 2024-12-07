class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def possible(max_num):
            curr = 0

            for num in nums:
                curr += ceil(num / max_num) - 1

                if curr > maxOperations:
                    return False

            return True

        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1

        return l