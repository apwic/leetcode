class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n

        for a, b in edges:
            indegree[b] += 1

        count = 0
        champ = -1

        for i in range(n):
            if count > 1:
                return -1

            if indegree[i] == 0:
                count += 1
                champ = i

        return champ if count == 1 else -1
