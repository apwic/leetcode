class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = 0
        curr_max = 0
        prev_max = 0

        for num in nums:
            if num.bit_count() != bits:
                bits = num.bit_count()
                prev_max = max(prev_max, curr_max)
            
            if num < prev_max:
                return False

            curr_max = max(curr_max, num)

        return True
