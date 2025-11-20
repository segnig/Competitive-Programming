# Problem: Unique Binary Search Trees - https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += dp[root - 1] * dp[nodes - root]
            dp[nodes] = total
        
        return dp[n]