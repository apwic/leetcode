class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        i1 = i2 = 0
        ans = []

        while i1 < n1 and i2 < n2:
            if nums1[i1][0] == nums2[i2][0]:
                ans.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
            elif nums1[i1][0] < nums2[i2][0]:
                ans.append([nums1[i1][0], nums1[i1][1]])
                i1 += 1
            else:
                ans.append([nums2[i2][0], nums2[i2][1]])
                i2 += 1

        while i1 < n1:
            ans.append([nums1[i1][0], nums1[i1][1]])
            i1 += 1

        while i2 < n2:
            ans.append([nums2[i2][0], nums2[i2][1]])
            i2 += 1

        return ans
