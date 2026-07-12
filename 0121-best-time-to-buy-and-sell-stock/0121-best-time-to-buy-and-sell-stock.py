class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        max_profit = 0
        for price in prices:
            if price < buyPrice :
                buyPrice = price
            else:
                profit = price - buyPrice
                if max_profit < profit :
                    max_profit = profit

        return max_profit
