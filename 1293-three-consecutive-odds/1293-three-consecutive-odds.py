class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def checkOdd(num):
            return num % 2 == 1

        n = len(arr)

        for i in range(2, n):
            if checkOdd(arr[i-2]) and checkOdd(arr[i-1]) and checkOdd(arr[i]):
                return True

        return False