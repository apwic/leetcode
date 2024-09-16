class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        times = []

        for time in timePoints:
            hour, minute = map(int, time.split(':'))
            total = hour * 60 + minute
            times.append(total)

        times.sort()
        DAY = 24 * 60

        for i in range(n):
            times.append(times[i] + DAY)

        diff = float('inf')
        for i in range(1, n*2):
            diff = min(diff, abs(times[i] - times[i-1]))

        return diff
