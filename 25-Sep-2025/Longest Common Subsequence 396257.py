# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1) + 1, len(text2) + 1

        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]

        for i in range(1, l2):
            for j in range(1, l1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[len(text2)][len(text1)]