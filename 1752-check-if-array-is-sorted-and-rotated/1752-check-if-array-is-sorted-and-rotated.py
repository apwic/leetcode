class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_sort = sorted(nums)
        min_num = nums_sort[0]
        idxs = []

        for i in range(n):
            if nums[i] == min_num:
                idxs.append(i)

        attempts = []
        for idx in idxs:
            curr = True
            for i in range(n):
                if nums[(i + idx) % n] != nums_sort[i]:
                    curr = False
                    break

            attempts.append(curr)

        ans = False
        for attempt in attempts:
            ans = ans or attempt

        return ans
