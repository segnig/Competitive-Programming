# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(col, row):
            if row == len(triangle):
                return 0
            if col == len(triangle[row]):
                return inf
            return triangle[row][col] + min(dp(col, row + 1), dp(col +1, row +1))

        return dp(0, 0)