class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(vis, s, d):
            if (s == d):
                return True
            
            vis[s] = 1
            
            for i in adj[s]:
                if (vis[i] == 0):
                    if dfs(vis, i, d):
                        return True
            
        adj = [[] for _ in range(n)]
 
        for edge in edges:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)
            
        vis = [0] * n
        for i in range(n):
            if (vis[i] == 0):
                if dfs(vis, source, destination):
                    return True
        
        return False
        
        
        
                    
            