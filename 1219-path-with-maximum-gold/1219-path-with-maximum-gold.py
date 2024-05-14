class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        def dfs(node, curr, visited=None):
            if visited is None:
                visited = []
           
            to_visit = []
            i, j = node[0], node[1]
            curr += grid[i][j]
            visited.append(node)
            
            for a, b in move:
                next_i = i + a
                next_j = j + b
                if (next_i >= 0 and next_i < m) and (next_j >= 0 and next_j < n) and grid[next_i][next_j] != 0 and [next_i, next_j] not in visited:
                    to_visit.append([next_i, next_j])
            
            if len(to_visit) == 0:
                return curr
            
            path = []
            for el in to_visit:
                path.append(dfs(el, curr, visited.copy()))
                
            return max(path)
        
        start = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    start.append([i, j])
                    
        if len(start) == 0:
            return 0

        path = []
        for node in start:
            path.append(dfs(node, 0, []))
            
        return max(path)
                