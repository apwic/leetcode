class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graphs = defaultdict(list)

        for node, parent in enumerate(parents):
            graphs[parent].append(node)

        freq = Counter()

        def dfs(node=0):
            product = 1
            total = 0

            for child in graphs[node]:
                count = dfs(child)
                product *= count
                total += count

            product *= max(1, n - 1 - total)
            freq[product] += 1

            return total + 1

        dfs()
        
        return freq[max(freq.keys())]
                