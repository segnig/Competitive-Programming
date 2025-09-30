# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return inf
            return min(grid[i][j] + dp(i -1, j), grid[i][j] + dp(i, j - 1))

        return dp(len(grid) - 1, len(grid[0]) - 1)