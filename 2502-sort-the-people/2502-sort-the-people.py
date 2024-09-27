class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        sort_idx = sorted(range(n), key=lambda x: heights[x], reverse=True)
        return [names[i] for i in sort_idx]