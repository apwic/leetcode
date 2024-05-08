class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks_idx = [num[0] for num in sorted(enumerate(score), key=lambda x: x[1], reverse=True)]
        medal = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        
        for i in range(len(ranks_idx)):
            rank_idx = ranks_idx[i]
            if i in medal:
                score[rank_idx] = medal[i]
            else:
                score[rank_idx] = str(i + 1)
                
        return score