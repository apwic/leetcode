class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0: heapq.heappush(pq, (-a, 'a'))
        if b > 0: heapq.heappush(pq, (-b, 'b'))
        if c > 0: heapq.heappush(pq, (-c, 'c'))

        ans = ""
        while pq:
            curr, char = heapq.heappop(pq)
            curr *= -1

            if len(ans) >= 2 and ans[-1] == char and ans[-2] == char:
                if not pq:
                    break

                next_curr, next_char = heapq.heappop(pq)
                next_curr *= -1
                ans += next_char
                next_curr -= 1

                if next_curr > 0:
                    heapq.heappush(pq, (-next_curr, next_char))
                heapq.heappush(pq, (-curr, char))
            else:
                ans += char
                curr -= 1

                if curr > 0:
                    heapq.heappush(pq, (-curr, char))

        return ans