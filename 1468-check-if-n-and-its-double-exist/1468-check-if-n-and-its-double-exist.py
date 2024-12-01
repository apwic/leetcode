class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1

        for num in arr:
            if num == 0 and freq[num] > 1:
                return True

            if num != 0 and freq[num*2]:
                return True

        return False