# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return -1
            if amt in memo:
                return memo[amt]

            min_count = float("inf")

            for coin in coins:
                res = dp(amt - coin)
                if res != -1:
                    min_count =  min(min_count, 1 + res)
        
            memo[amt] = min_count if min_count != float('inf') else -1

            return memo[amt]
        
        return dp(amount)