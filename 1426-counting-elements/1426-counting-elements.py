class Solution:
    def countElements(self, arr: List[int]) -> int:
        st = set(arr)
        tot = 0

        for i in arr:
            if i + 1 in st:
                tot += 1

        return tot