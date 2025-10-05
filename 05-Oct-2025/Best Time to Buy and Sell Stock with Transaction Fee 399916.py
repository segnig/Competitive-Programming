# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        profit, hold = 0, -inf

        for price in prices:
            profit = max(profit, hold + price - fee)
            hold = max(hold, profit - price)
        
        return profit