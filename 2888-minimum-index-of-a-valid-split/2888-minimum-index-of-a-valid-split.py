class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1

        max_key = -1
        max_freq = 0
        for key in freq.keys():
            if freq[key] > max_freq:
                max_key = key
                max_freq = freq[key]

        if max_freq <= n//2:
            return -1

        curr_freq = defaultdict(int)
        for i in range(n-1):
            curr_freq[nums[i]] += 1
            split1, split2 = curr_freq[max_key], max_freq - curr_freq[max_key]
            split_len = i+1

            if split1 > split_len//2 and split2 > (n-split_len)//2:
                return i

        return -1