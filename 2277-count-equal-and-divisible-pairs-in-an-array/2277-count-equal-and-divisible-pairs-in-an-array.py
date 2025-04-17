class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(list)

        for i in range(n):
            freq[nums[i]].append(i)

        ans = 0
        for arr in freq.values():
            length = len(arr)
            for i in range(length):
                for j in range(i+1, length):
                    if (arr[i] * arr[j]) % k == 0:
                        ans += 1

        return ans
