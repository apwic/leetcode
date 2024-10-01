class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)

        for num in arr:
            rem = (num % k + k) % k
            freq[rem] += 1

        for num in arr:
            rem = (num % k + k) % k

            if rem == 0:
                if freq[rem] % 2 == 1:
                    return False
            elif freq[rem] != freq[k-rem]:
                return False

        return True