class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        idx_map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                idx_map[stack.pop()] = num
                
            stack.append(num)

        ans = []
        for num in nums1:
            if num in idx_map:
                ans.append(idx_map[num])
            else:
                ans.append(-1)

        return ans
