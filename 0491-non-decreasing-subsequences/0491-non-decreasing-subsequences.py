class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(idx=0, curr=[], ans=set()):
            if idx == n:
                if len(curr) >= 2:
                    ans.add(tuple(curr))
                return ans

            ans = backtrack(idx+1, curr, ans)

            if (curr and curr[-1] <= nums[idx]) or not curr:
                curr.append(nums[idx])
                ans = backtrack(idx+1, curr, ans)
                curr.pop()

            return ans

        ans = backtrack()
        return [list(seq) for seq in ans]