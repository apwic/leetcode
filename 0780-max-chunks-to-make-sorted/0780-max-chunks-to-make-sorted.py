class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        counter = [0] * n
        count = 0

        for i in range(n):
            counter[arr[i]] = 1

            if sum(counter[:i+1]) == i+1:
                count += 1

        return count