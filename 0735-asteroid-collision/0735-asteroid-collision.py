class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if (len(asteroids) == 1):
            return asteroids
        
        i = 0
        j = i + 1
        while (i < len(asteroids) - 1 and j < len(asteroids)):
            # colliding
            if (asteroids[i] > 0 and asteroids[j] < 0):
                a = abs(asteroids[i])
                b = abs(asteroids[j])
                if (a > b):
                    asteroids.pop(j)
                elif (a == b):
                    asteroids.pop(i)
                    asteroids.pop(i)
                else:
                    asteroids.pop(i)
                i = 0
                j = i + 1
            else:
                i += 1
                j += 1
                continue
                
        return asteroids
                    
                
                