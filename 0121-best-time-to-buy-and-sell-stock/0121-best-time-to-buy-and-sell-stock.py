class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        max_profit = 0
        for price in prices:
            profit = price - buyPrice 
            if profit > max_profit :
                max_profit = profit
            if profit < 0 :
                buyPrice = price

        return max_profit
