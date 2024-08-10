class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        def backtrack(idx=0, curr=[], ans=[]):
            sum_curr = sum(curr)
            if sum_curr == target:
                ans.append(curr[:])
                return 

            if sum_curr > target:
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                    
                curr.append(candidates[i])
                backtrack(i+1, curr, ans)
                curr.pop()

            return ans

        return backtrack()