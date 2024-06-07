class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    break
                j += 1

            greater = -1
            j += 1
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    greater = nums2[j]
                    break
                j += 1

            ans.append(greater)
        
        return ans


