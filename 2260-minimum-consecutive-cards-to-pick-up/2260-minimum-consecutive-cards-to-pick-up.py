class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_idx = {}
        ans = -1
        
        for idx, val in enumerate(cards):
            if val in last_idx:
                temp = idx-last_idx[val] + 1
                ans = min(ans, temp) if ans != -1 else temp
            
            last_idx[val] = idx
            
        return ans
        
        