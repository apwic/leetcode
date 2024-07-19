class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        seen = set()
        def backtrack(idx=1,curr=[],arr=[]):
            if len(curr) == k:
                arr.append(curr[:])
                return arr

            for nums in range(idx, n+1):
                curr.append(nums)
                arr = backtrack(nums+1, curr, arr)
                curr.pop()

            return arr

        return backtrack()
        