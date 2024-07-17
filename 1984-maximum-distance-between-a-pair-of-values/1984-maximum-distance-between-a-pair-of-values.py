class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(l, r, boundary):
            while l <= r:
                mid = (l+r)//2
                if nums2[mid] >= boundary:
                    l = mid+1
                else:
                    r = mid-1
            
            return r

        n1, n2 = len(nums1), len(nums2)
        ans = 0
        for i in range(n1):
            if i < n2 and nums1[i] <= nums2[i]:
                search = binary_search(i, n2-1, nums1[i])
                ans = max(ans, search-i)

        return ans
                