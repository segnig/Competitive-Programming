# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1] *m for _ in range(n)]

        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[n -1][m-1]