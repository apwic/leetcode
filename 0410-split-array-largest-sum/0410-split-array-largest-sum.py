class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(boundary):
            n, curr = 0, 0
            for num in nums:
                if curr + num <= boundary:
                    curr += num
                else:
                    n += 1
                    curr = num

            return n+1 <= k

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1

        return l
        