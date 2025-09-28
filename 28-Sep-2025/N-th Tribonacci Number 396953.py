# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        @cache
        def dp(i):
            if i < 3:
                return int(i != 0)
            result = dp(i-1) + dp(i-2) + dp(i-3) 
            return result
        return dp(n)