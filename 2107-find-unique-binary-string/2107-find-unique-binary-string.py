class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        def backtrack(curr = []):
            if len(curr) == n:
                bin_str = "".join(curr[:])
                if bin_str not in nums:
                    return bin_str
                else:
                    return ""

            for ch in ["0", "1"]:
                curr.append(ch)
                ans = backtrack(curr)
                if ans:
                    return ans
                curr.pop()

            return ans

        return backtrack()