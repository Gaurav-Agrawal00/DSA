class Solution:
    def candy(self, ratings: List[int]) -> int:
        sum1 = 1
        n = len(ratings)
        i = 1
        while i < n:
            if ratings[i] == ratings[i-1]:
                sum1 += 1
                i += 1
                continue
            
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                sum1 += peak 
                i += 1
            
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                sum1 += down 
                i += 1
                down += 1
            if down > peak :
                sum1 += down - peak
        return sum1