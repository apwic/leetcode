class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source, target = 0, len(graph)-1
        def backtrack(node, path=[source], ans=[]):
            if node == target:
                ans.append(path[:])
                return ans

            for neighbor in graph[node]:
                path.append(neighbor)
                ans = backtrack(neighbor, path, ans)
                path.pop()

            return ans

        return backtrack(source)
        