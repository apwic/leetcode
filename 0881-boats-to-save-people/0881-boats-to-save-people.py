class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        
        if n == 1:
            return 1
    
        people = sorted(people)
        ans = 0
        i, j = 0, n - 1
        
        while i <= j:
            a, b = people[i], people[j]
            if a + b <= limit:
                i += 1
            
            j -= 1
            ans += 1

        return ans
        
        