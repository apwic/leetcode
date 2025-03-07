class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for num in range(2, int(right**0.5) + 1):
            if sieve[num]:
                for mul in range(num * num, right + 1, num):
                    sieve[mul] = False

        primes = [num for num in range(left, right + 1) if sieve[num]]

        if len(primes) < 2:
            return -1, -1

        min_diff = float('inf')
        ans = (-1, -1)

        for i in range(1, len(primes)):
            a, b = primes[i-1], primes[i]
            diff = b - a

            if diff < min_diff:
                min_diff = diff
                ans = a, b

        return ans