class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = [nums[i] for i in range(n) if i % 2 == 0]
        odd = [nums[i] for i in range(n) if i % 2 == 1]
        
        even.sort()
        odd.sort(reverse=True)

        ans = []
        i, j, k = 0, 0, 0
        while k < n:
            if k % 2 == 0:
                ans.append(even[i])
                i += 1
            else:
                ans.append(odd[j])
                j += 1
            k += 1

        return ans