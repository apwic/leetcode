class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, max(ranks) * cars * cars

        while l < r:
            mid = (l + r) // 2
            repair = sum(int((mid/rank)**0.5) for rank in ranks)
            
            if repair < cars:
                l = mid + 1
            else:
                r = mid

        return l