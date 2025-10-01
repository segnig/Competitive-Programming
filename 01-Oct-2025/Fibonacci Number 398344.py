# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        first, second = 0, 1

        for _ in range(2, n):
            second, first = second + first, second
        return second + first