class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        x1, x2 = 0, 0

        if n2 % 2 == 1:
            for num in nums1:
                x1 ^= num

        if n1 % 2 == 1:
            for num in nums2:
                x2 ^= num

        return x1 ^ x2
