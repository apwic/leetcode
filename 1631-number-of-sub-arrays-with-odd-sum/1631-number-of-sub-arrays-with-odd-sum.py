class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        parity = [num % 2 for num in arr]
        count = prefix = 0
        odd = 0
        even = 1

        for p in parity:
            prefix += p

            if prefix % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

            count %= MOD

        return count