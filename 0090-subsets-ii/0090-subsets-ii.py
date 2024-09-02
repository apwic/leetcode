class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        def backtrack(idx=0, arr=[], ans=[]):
            ans.append(arr[:])

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()

            return ans

        return backtrack()