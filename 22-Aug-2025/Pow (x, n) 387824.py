# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def power(x, n):
            if n == 1:
                return x
            res = self.myPow(x, n//2)
            res *= res
            return res * x if n % 2 == 1 else res
        return power(x, n) if n > 0 else 1/power(x, -n)