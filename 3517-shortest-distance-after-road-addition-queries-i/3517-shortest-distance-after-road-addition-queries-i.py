class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dp():
            memo = [i for i in range(n-1, -1, -1)]
            memo.append(0)

            for node in range(n-2, -1, -1):
                min_dist = n
                for neighbor in graphs[node]:
                    min_dist = min(min_dist, memo[neighbor] + 1)

                memo[node] = min_dist

            return memo[0]

        graphs = defaultdict(set)

        for i in range(n):
            graphs[i].add(i+1)

        res = []
        for a, b in queries:
            graphs[a].add(b)
            res.append(dp())

        return res