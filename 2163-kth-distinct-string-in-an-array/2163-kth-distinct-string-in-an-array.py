class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = []
        freq = defaultdict(int)

        for ch in arr:
            freq[ch] += 1

        curr = 1
        for ch in arr:
            if freq[ch] == 1: 
                if curr == k:
                    return ch
                else:
                    curr += 1
                    
        return ""