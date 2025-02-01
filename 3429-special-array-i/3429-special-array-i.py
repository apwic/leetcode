class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for i in range(1, len(nums)):
            curr = nums[i] % 2
            if parity == curr:
                return False

            parity = curr
            
        return True