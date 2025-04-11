class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def sumStr(num):
            sum_num = 0
            for ch in num:
                sum_num += int(ch)

            return sum_num

        ans = 0
        for num in range(low, high+1):
            str_num = str(num)
            n = len(str_num)
            if n % 2 != 0:
                continue

            first = str_num[:n//2]
            second = str_num[(n//2):]
            if sumStr(first) == sumStr(second):
                ans += 1

        return ans