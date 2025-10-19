# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x :x[0] - x[1]) 
        total_cost = 0

        for i in range(len(costs)):
            total_cost += costs[i][i>=len(costs)//2]
        
        return total_cost