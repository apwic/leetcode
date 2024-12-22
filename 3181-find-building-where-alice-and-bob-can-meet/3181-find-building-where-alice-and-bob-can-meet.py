class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def search(height, stack):
            l = 0
            r = len(stack) - 1
            pos = -1
            while l <= r:
                mid = (l+r) // 2
                if stack[mid][0] > height:
                    pos = max(pos, mid)
                    l = mid + 1
                else:
                    r = mid - 1

            return pos
            
        n = len(heights)
        q = len(queries)

        stack = []
        new_queries = [[] for _ in range(n)]
        ans = [-1 for _ in range(q)]

        for i in range(q):
            a, b = queries[i][0], queries[i][1]

            if a > b:
                a, b = b, a

            if a == b or heights[b] > heights[a]:
                ans[i] = b
            else:
                # only search when a < b and heights[a] > heights[b]
                new_queries[b].append((heights[a], i))

        for i in range(n-1, -1, -1):
            size = len(stack)

            for height, query in new_queries[i]:
                pos = search(height, stack)
                if 0 <= pos and pos < size:
                    ans[query] = stack[pos][1]

            while stack and stack[-1][0] <= heights[i]:
                stack.pop()

            stack.append((heights[i], i))

        return ans