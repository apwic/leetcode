class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        memo = [[0 for _ in range(n)] for _ in range(n)]
        
        def part(start, chunks):
            if start == n:
                ans.append(chunks[:])
                return
            
            for end in range(start, n):
                chunk = s[start:end+1]
                # if not checked in memo
                if not memo[start][end]:
                    if chunk == chunk[::-1]:
                        memo[start][end] = 1
                  
                if memo[start][end]:
                    part(end+1, chunks + [chunk])
                    
        part(0, [])
        return ans
                
            
        
        
            
            
            
            
        