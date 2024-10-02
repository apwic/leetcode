class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = sorted(arr)
        freq = defaultdict(int)
        rank = 1
        
        for num in arr_sort:
            if not freq[num]:
                freq[num] = rank
                rank += 1

        ans = []
        for num in arr:
            ans.append(freq[num])

        return ans