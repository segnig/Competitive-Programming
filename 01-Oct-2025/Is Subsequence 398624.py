# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[0] = [1] * (len(t) + 1) 

        for row in range(1, len(s) + 1):
            for col in range(1, len(t) + 1):
                if s[row-1] == t[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = dp[row][col-1]

        return dp[len(s)][len(t)] == 1