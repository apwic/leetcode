class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()
        ans = []

        for spell in spells:
            l, r = 0, m-1
            while l <= r:
                mid = (l+r)//2
                target = potions[mid] * spell
                if target < success:
                    l = mid+1
                else:
                    r = mid-1

            ans.append(m-l)

        return ans
        