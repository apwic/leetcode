class Solution:
    def minMaxDifference(self, num: int) -> int:
        minNum = maxNum = str(num)
        n = len(minNum)
        i = 0

        while i < n and maxNum[i] == "9":
            i += 1

        if i < n:
            maxNum = maxNum.replace(maxNum[i], "9")

        minNum = minNum.replace(minNum[0], "0")
        return int(maxNum) - int(minNum)