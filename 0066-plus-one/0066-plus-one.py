class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numbers = int("".join(map(str, digits)))
        numbers += 1

        return map(int, [*str(numbers)])