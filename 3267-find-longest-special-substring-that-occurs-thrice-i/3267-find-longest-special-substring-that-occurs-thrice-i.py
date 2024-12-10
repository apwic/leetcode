class Solution:
    def maximumLength(self, s: str) -> int:
        freq = defaultdict(int)

        for i in range(len(s)):
            freq[s[i]] += 1
            curr = [s[i]]
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    break

                curr.append(s[j])
                freq["".join(curr)] += 1
            
        ans = []
        for key, val in freq.items():
            if val >= 3:
                print(key, val)
                ans.append(len(key))
            
        if len(ans) == 0:
            return -1

        return max(ans)