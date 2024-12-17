class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1

        heap = []
        for key in freq:
            heap.append((-ord(key), freq[key]))

        heapify(heap)
        ans = []

        while heap:
            char_neg, count = heappop(heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)
            # add max of char that can be used
            ans.append(char * use)

            # count is larger than use
            # need to find the next element to fill next
            if count > use and heap:
                next_char, next_count = heappop(heap)
                ans.append(chr(-next_char))

                if next_count > 1:
                    heappush(heap, (next_char, next_count-1))

                heappush(heap, (char_neg, count - use))

        return "".join(ans)
