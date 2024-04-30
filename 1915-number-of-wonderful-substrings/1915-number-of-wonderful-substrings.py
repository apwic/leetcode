class Solution:
    from collections import defaultdict
    def wonderfulSubstrings(self, word: str) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        bitmask = 0
        count = 0
                
        for char in word:
            bitmask = bitmask ^ (1 << ord(char) - ord('a'))
            count += freq[bitmask]
            
            for i in range(10):
                flip = bitmask ^ (1 << i)
                count += freq[flip]
                
            freq[bitmask] += 1
        
        return count
                