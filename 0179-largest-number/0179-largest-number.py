class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        nums = list(map(str, nums))
        sorted_nums = sorted(nums, key=cmp_to_key(compare))

        if sorted_nums[0] == "0":
            return "0"

        return ''.join(sorted_nums)
