class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        for i in range(n):
            times[i].append(i)

        times.sort()
        chairs = []
        departure = []
        next_chair = 0

        for time in times:
            arrival, leave, idx = time

            while departure and departure[0][0] <= arrival:
                _, chair = heapq.heappop(departure)
                heapq.heappush(chairs, chair)

            if chairs:
                curr_chair = heapq.heappop(chairs)
            else:
                curr_chair = next_chair
                next_chair += 1

            heapq.heappush(departure, (leave, curr_chair))

            if idx == targetFriend:
                return curr_chair

        return 0