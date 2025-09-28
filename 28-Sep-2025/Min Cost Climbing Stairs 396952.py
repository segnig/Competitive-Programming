# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = {}

        def dp(ind):
            if ind < 0:
                return 0
            if ind not in memo:
                one = cost[ind] + dp(ind - 1)
                two = cost[ind] + dp(ind - 2)
                memo[ind] = min(one, two)

            return memo[ind]

        return dp(len(cost) - 1)

        