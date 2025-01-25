class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        nums.sort()

        i = 0
        ans = [0] * n
        while i < n:
            j = i+1
            idx = [nums[i][1]]
            while j < n and nums[j][0] - nums[j-1][0] <= limit:
                idx.append(nums[j][1])
                j += 1

            heapify(idx)
            for k in range(i, j):
                pop = heappop(idx)
                ans[pop] = nums[k][0]

            i = j

        return ans
