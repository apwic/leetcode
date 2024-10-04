class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        sums = sum(skill)

        if n == 2:
            return skill[0] * skill[1]

        if sums % (n/2) != 0:
            return -1

        need = sums // (n/2)
        skill.sort()

        i, j = 0, n-1
        ans = []
        while i < j:
            if skill[i] + skill[j] == need:
                ans.append((skill[i], skill[j]))
                i += 1
                j -= 1
            else:
                return -1
            
        return sum([a*b for a, b in ans])