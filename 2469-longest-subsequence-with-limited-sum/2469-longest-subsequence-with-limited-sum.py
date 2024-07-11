class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[i-1] + nums[i])

        ans = []

        for query in queries:
            l, r = 0, n-1 
            while l <=r :
                mid = (l+r)//2
                if prefix[mid] > query:
                    r = mid-1
                else:
                    l = mid+1

            ans.append(l)

        return ans
        