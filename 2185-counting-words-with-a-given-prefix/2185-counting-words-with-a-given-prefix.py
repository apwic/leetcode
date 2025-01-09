class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n_pref = len(pref)
        ans = 0
        for word in words:
            if n_pref > len(word):
                continue

            if pref == word[:n_pref]:
                ans += 1

        return ans