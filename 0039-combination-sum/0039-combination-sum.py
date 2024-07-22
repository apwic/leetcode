class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def backtrack(idx=0, curr=[], arr=[]):
            sum_curr = sum(curr)
            if sum_curr == target:
                arr.append(curr[:])
                return arr

            if sum_curr > target:
                return arr

            for curr_idx in range(idx,n):
                curr.append(candidates[curr_idx])
                arr = backtrack(curr_idx, curr, arr)
                curr.pop()

            return arr

        return backtrack()
        