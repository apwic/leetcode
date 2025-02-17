class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def sequences(freq):
            total = 0

            for pos in range(26):
                if freq[pos] == 0:
                    continue

                total += 1
                freq[pos] -= 1
                total += sequences(freq)
                freq[pos] += 1

            return total
            
        A = ord('A')
        freq = [0] * 26
        for ch in tiles:
            freq[ord(ch) - A] += 1

        return sequences(freq)
