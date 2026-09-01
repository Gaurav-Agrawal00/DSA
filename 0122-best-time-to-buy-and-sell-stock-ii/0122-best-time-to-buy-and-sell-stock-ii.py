class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        bp = float('inf')
        for price in prices:
            if price < bp:
                bp = price
            else:
                mProfit += price - bp
                bp = price
        return mProfit