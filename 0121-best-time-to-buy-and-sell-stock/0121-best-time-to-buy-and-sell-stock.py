class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10**4 + 1
        mx = -1
        mn_i = mx_i = 0
        ans = 0
        
        for i in range(len(prices)):
            if (prices[i] < mn):
                mn = prices[i]
                mn_i = i
                
            if (prices[i] > mx):
                mx = prices[i]
                mx_i = i
            
            if (mn_i < mx_i):
                ans = max(ans, mx - mn)
            else:
                mx = prices[i]
                mx_i = i
            
        return ans