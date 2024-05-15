class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        if n == 1:
            return 0
        
        distance_grid = [[math.inf]*n for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    distance_grid[i][j] = 0
        
        while queue:
            i, j = queue.popleft()
            
            for d_i, d_j in directions:
                n_i, n_j = i + d_i, j + d_j
                    
                if (0 <= n_i < n) and (0 <= n_j < n) and distance_grid[n_i][n_j] == math.inf:
                    distance_grid[n_i][n_j] = distance_grid[i][j] + 1
                    queue.append((n_i, n_j))    
            
        pq = [(-distance_grid[0][0], 0, 0)]
        heapq.heapify(pq)
        max_safe = [[-1]*n for _ in range(n)]
        max_safe[0][0] = distance_grid[0][0]
        
        while pq:
            distance, i, j = heapq.heappop(pq)
            distance = -distance
            
            if i == n-1 and j == n-1:
                return distance
            
            for d_i, d_j in directions:
                n_i, n_j = i + d_i, j + d_j
                
                if (0 <= n_i < n) and (0 <= n_j < n):
                    n_distance = min(distance, distance_grid[n_i][n_j])
                    if n_distance > max_safe[n_i][n_j]:
                        max_safe[n_i][n_j] = n_distance
                        heapq.heappush(pq, (-n_distance, n_i, n_j))
        
        return -1