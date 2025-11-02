# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # [[10,20],[30,200],[400,50],[30,20]]
        #   10, 170, -350, -10
        
        costs.sort(key =lambda cost: cost[1] - cost[0])

        total_cost = 0
        for index, _ in enumerate(costs):
            total_cost += costs[index][index < len(costs) // 2]
        
        return total_cost

