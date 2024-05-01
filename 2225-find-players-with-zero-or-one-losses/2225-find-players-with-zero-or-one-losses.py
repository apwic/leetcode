class Solution:
    from collections import defaultdict
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        freq = defaultdict(int)
        
        for match in matches:
            freq[match[0]] += 0
            freq[match[1]] += 1
            
        ans = [[], []]
        
        for key, val in freq.items():
            if val == 0:
                ans[0].append(key)
            if val == 1:
                ans[1].append(key)
                
        ans[0] = sorted(ans[0])
        ans[1] = sorted(ans[1])
        return ans