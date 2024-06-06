class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc, dec = deque(), deque()
        ans = 0
        l = 0

        for r in range(len(nums)):
            while inc and nums[inc[-1]] > nums[r]:
                inc.pop() 
            inc.append(r)
            
            while dec and nums[dec[-1]] < nums[r]:
                dec.pop()
            dec.append(r)

            while nums[dec[0]] - nums[inc[0]] > limit:
                l += 1
                if inc[0] < l:
                    inc.popleft()
                if dec[0] < l:
                    dec.popleft()
            
            ans = max(ans, r-l+1)
        return ans