class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        total = 0
        k = 0
        diff = [0] * (n + 1)

        for i in range(n):
            while total + diff[i] < nums[i]:
                k += 1

                if k > m:
                    return -1 

                l, r, val = queries[k-1]

                if r >= i:
                    diff[max(l, i)] += val
                    diff[r+1] -= val
                
            total += diff[i]

        return k