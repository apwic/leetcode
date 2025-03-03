class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        count = 0

        for num in nums:
            if num == pivot:
                count += 1
                continue

            if num < pivot:
                before.append(num)
            else:
                after.append(num)

        return before + [pivot] * count + after