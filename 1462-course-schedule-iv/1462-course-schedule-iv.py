from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graphs = defaultdict(list)
        for a, b in prerequisites:
            graphs[a].append(b)
        
        prereq_sets = [set() for _ in range(numCourses)]
        
        def bfs(node):
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                for neighbor in graphs[curr]:
                    if neighbor not in prereq_sets[node]: 
                        prereq_sets[node].add(neighbor)
                        queue.append(neighbor)

        for i in range(numCourses):
            bfs(i)
        
        ans = []
        for u, v in queries:
            ans.append(v in prereq_sets[u])
        
        return ans
