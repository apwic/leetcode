class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def DFS(curr=1, ans=[]):
            if curr > n:
                return ans
            else:
                ans.append(curr)

            for i in range(10):
                nxt = curr * 10 + i

                if nxt <= n:
                    DFS(nxt, ans)

            return ans

        ans = []
        for i in range(1, 10):
            DFS(curr=i, ans=ans)

        return ans