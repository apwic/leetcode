class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        heaps = [(-profits[i], capital[i]) for i in range(n)]
        temps = []
        heapq.heapify(heaps)

        while k and heaps:
            profit, cap = heapq.heappop(heaps)

            if w >= cap:
                w -= profit
                k -= 1

                for temp in temps:
                    heapq.heappush(heaps, temp)
                temps = []
            else:
                temps.append((profit, cap))

        return w