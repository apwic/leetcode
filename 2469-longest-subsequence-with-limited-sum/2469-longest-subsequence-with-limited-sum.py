class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []

        for query in queries:
            curr, curr_sum = 0, 0
            for num in nums:
                if curr_sum + num <= query:
                    curr += 1
                    curr_sum += num
                else:
                    break

            ans.append(curr)

        return ans
        