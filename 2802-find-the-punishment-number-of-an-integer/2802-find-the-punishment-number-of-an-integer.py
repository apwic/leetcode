class Solution:
    def punishmentNumber(self, n: int) -> int:
        # RUN THIS TO GET ALL THE POSSIBLE NUM
        # THE NUM IS SMALL SO THE RESULT IS SMALL

        # def partition(s, target):
        #     if not s and target == 0:
        #         return True

        #     if target < 0:
        #         return False

        #     for i in range(len(s)):
        #         l, r = s[:i+1], s[i+1:]
        #         l_num = int(l)

        #         if partition(r, target - l_num):
        #             return True

        #     return False

        # possible = []
        # for num in range(1, 1001):
        #     if partition(str(num*num), num):
        #         possible.append(num)

        # print(possible)

        # LOAD THE POSSIBLE NUM
        possible = [0, 1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]

        return sum([num*num for num in possible if num <= n])
        