class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        for i in range(n):
            curr = 0
            for j in range(1, k+1 if k > 0 else -k+1):
                if k < 0:
                    j *= -1

                curr += code[(i+j) % n]

            ans[i] = curr

        return ans
                