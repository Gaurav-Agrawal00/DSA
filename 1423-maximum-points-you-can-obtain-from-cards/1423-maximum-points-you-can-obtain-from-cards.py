class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_ = 0

        for i in range(k):
            sum_ = sum_ + cardPoints[i]

        maxSum = sum_
        l = k - 1
        r = len(cardPoints) - 1
        while l >= 0:
            sum_ = sum_ - cardPoints[l] + cardPoints[r]
            l -= 1
            r -= 1
            maxSum = max(maxSum, sum_)
        return maxSum
