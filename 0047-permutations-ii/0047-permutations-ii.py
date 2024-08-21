class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack(curr=[], arr_idx=[], ans=[]):
            if len(curr) == n:
                if curr not in ans:
                    ans.append(curr[:])
                return

            for i in range(n):
                if i not in arr_idx:
                    arr_idx.append(i)
                    curr.append(nums[i])
                    backtrack(curr, arr_idx, ans)
                    arr_idx.pop()
                    curr.pop()

            return ans

        return backtrack()