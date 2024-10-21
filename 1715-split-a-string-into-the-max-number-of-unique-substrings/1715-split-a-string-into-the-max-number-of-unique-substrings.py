class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def backtrack(idx=0, track=[], ans=0):
            if idx == n:
                return max(ans, len(track))

            for i in range(idx, n):
                if s[idx:i+1] not in track:
                    track.append(s[idx:i+1])
                    ans = backtrack(i+1, track, ans)
                    track.pop()

            return ans

        return backtrack()
