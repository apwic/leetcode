class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end+1, -1))

        events.sort()

        ans = 0
        curr = 0
        for _, delta in events:
            curr += delta
            ans = max(ans, curr)

        return ans