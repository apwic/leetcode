class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        max_sum = 0
        count_neg = 0
        min_abs = float('inf')

        for row in matrix:
            for num in row:
                if num < 0:
                    count_neg += 1

                abs_num = abs(num)
                min_abs = min(min_abs, abs_num)
                max_sum += abs_num

        if count_neg % 2 == 1:
            max_sum -= 2 * min_abs

        return max_sum