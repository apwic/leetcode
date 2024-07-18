class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(curr=[], arr=[]):
            if len(curr) == n:
                arr.append(curr[:])
                return arr

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    arr = backtrack(curr, arr)
                    curr.pop()
                    
            return arr
        
        return backtrack()