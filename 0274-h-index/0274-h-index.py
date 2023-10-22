from collections import defaultdict
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        freq = defaultdict(int)
        
        for i in range(1, n + 1):
            for x in citations:
                if x >= i:
                    freq[i] += 1
            
        ans = 0
        for i in freq:
            if (freq[i] >= ans and freq[i] >= i):
                ans = i
                
        return ans
        