class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]

        for enc in encoded:
            ans.append(ans[-1] ^ enc)

        return ans