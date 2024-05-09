class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        happiness = sorted(happiness, reverse=True)
        for i in range(len(happiness)):
            val = happiness[i]
            
            if k <= 0:
                break
                
            if val - i > 0:
                total += val - i
                k -= 1
            
        return total