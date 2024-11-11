class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime = [1] * (1001)
        prime[1] = 0
        for i in range(2, int(math.sqrt(1001)) + 1):
            if prime[i] == 1:
                for j in range(i * i, 1001, i):
                    prime[j] = 0

        curr = 1
        i = 0
        n = len(nums)
        while i < n:
            diff = nums[i] - curr

            if diff < 0:
                return False

            if prime[diff] or diff == 0:
                i += 1
                curr += 1
            else:
                curr += 1

        return True
                