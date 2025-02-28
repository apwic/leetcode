class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        prev_row = [str2[0:col] for col in range(n2 + 1)]

        for row in range(1, n1 + 1):
            curr_row = [str1[0:row]]+ [None for _ in range(n2)]

            for col in range(1, n2 + 1):
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    prev_s1 = prev_row[col]
                    prev_s2 = curr_row[col - 1]

                    curr_row[col] = (
                        prev_s1 + str1[row - 1]
                        if len(prev_s1) < len(prev_s2)
                        else prev_s2 + str2[col - 1]
                    )

            prev_row = curr_row

        return prev_row[n2]