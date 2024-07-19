class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ans = []
        def backtrack(idx, arr=[]):
            if idx == n:
                self.ans.append(arr[:])
                return 

            backtrack(idx+1, arr[:])
            arr.append(nums[idx])
            backtrack(idx+1, arr[:])

        backtrack(0)
        return self.ans