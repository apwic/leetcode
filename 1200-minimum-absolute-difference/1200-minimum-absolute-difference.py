class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # need to sort the arr
        n = len(arr)
        arr.sort()

        # find the min diff?
        min_diff = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - arr[i-1] < min_diff:
                min_diff = arr[i] - arr[i-1] 

        ans = []
        for i in range(1, n):
            if min_diff == arr[i] - arr[i-1] :
                ans.append([arr[i-1], arr[i]])

        return ans