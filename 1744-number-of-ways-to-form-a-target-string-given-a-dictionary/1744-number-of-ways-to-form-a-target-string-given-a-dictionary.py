class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n_word = len(words[0])
        n_target = len(target)
        mod = 1000000007

        freq = [[0] * 26 for _ in range(n_word)]
        for word in words:
            for j in range(n_word):
                freq[j][ord(word[j]) - ord("a")] += 1

        dp = [[0] * (n_target + 1) for _ in range(n_word + 1)]

        for curr_word in range(n_word + 1):
            dp[curr_word][0] = 1

        for curr_word in range(1, n_word + 1):
            for curr_target in range(1, n_target + 1):
                dp[curr_word][curr_target] = dp[curr_word - 1][curr_target]

                cur_pos = ord(target[curr_target - 1]) - ord("a")
                dp[curr_word][curr_target] += (
                    freq[curr_word - 1][cur_pos]
                    * dp[curr_word - 1][curr_target - 1]
                ) % mod
                dp[curr_word][curr_target] %= mod

        return dp[n_word][n_target]