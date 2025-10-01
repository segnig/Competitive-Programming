# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        temp = []

        for i in range(1, int(sqrt(n))+1):
            temp.append(i*i)
        @cache
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return inf
            
            result = inf
            for num in temp:
                result = min(result, 1 + dp(rem - num))

            return result
        
        return dp(n)
