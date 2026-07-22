class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0] * len(prices)
        stack = []
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            if stack :
                ans[i] = prices[i] - stack[-1]
            else:
                ans[i] = prices[i]
            stack.append(prices[i])
        return ans