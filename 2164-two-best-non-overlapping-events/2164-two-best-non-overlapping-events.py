class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        pq = []
        events.sort(key= lambda x: x[0])
        max_curr, ans = 0, 0

        for event in events:
            while pq and event[0] > pq[0][0]:
                max_curr = max(max_curr, heappop(pq)[1])

            ans = max(ans, max_curr + event[2])

            heapq.heappush(pq, (event[1], event[2]))

        return ans