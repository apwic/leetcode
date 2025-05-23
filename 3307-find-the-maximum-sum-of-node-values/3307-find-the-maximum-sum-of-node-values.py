class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        netChange = [(nums[i] ^ k) - nums[i] for i in range(n)]
        nodeSum = sum(nums)

        netChange.sort(reverse=True)

        for i in range(0, n, 2):
            # If netChange contains odd number of elements break the loop
            if i + 1 == n:
                break
            pairSum = netChange[i] + netChange[i + 1]
            # Include in nodeSum if pairSum is positive
            if pairSum > 0:
                nodeSum += pairSum

        return nodeSum