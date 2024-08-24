class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        
        for num in nums:
            # add to one, dont add from two
            one = (one ^ num) & ~two
            # add to two, if not in one
            two = (two ^ num) & ~one

        # only element one remain
        return one