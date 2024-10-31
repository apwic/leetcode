class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factory_flat = []

        for f in factory:
            factory_flat.extend([f[0]] * f[1])

        robot_count = len(robot)
        factory_count = len(factory_flat)
        dp = [[0 for _ in range(factory_count + 1)] for _ in range(robot_count+1)]

        for i in range(robot_count):
            dp[i][factory_count] += float('inf')

        for i in range(robot_count-1, -1, -1):
            for j in range(factory_count-1, -1, -1):
                take = abs(robot[i] - factory_flat[j]) + dp[i+1][j+1]
                skip = dp[i][j+1]

                dp[i][j] = min(take, skip)

        return dp[0][0]