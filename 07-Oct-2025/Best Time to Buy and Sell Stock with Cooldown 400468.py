# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo ={}
        def dp(i, is_buy):
            if i >= len(prices):
                return 0

            if (i, is_buy) in memo:
                return memo[(i, is_buy)]

            buy, sell, not_buy, not_sell = 0, 0, 0, 0
            if is_buy:
                buy = - prices[i] + dp(i+1, not is_buy)
                not_buy = dp(i+1, is_buy)
            else:
                sell = buy = prices[i] + dp(i+2, not is_buy)
                not_sell = dp(i+1, is_buy)
            memo[(i, is_buy)] = max([buy, not_buy, sell, not_sell])
            return memo[(i, is_buy)]
        
        return dp(0, True)
