class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        queue = deque()
        result = float('inf')
        
        for i in range(n + 1):
            while queue and prefix[i] - prefix[queue[0]] >= k:
                result = min(result, i - queue.popleft())
            
            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        
        return result if result != float('inf') else -1