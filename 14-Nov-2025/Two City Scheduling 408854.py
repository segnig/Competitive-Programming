# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key =lambda cost: cost[1] - cost[0])

        total_cost = 0
        for index, _ in enumerate(costs):
            total_cost += costs[index][index < len(costs) // 2]
        
        return total_cost

