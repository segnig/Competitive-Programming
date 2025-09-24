# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fn(n):
            if n < 2:
                return n
            if n not in memo:
                memo[n] =  fn(n-1) + fn(n-2)
            return memo[n]
        
        return fn(n)