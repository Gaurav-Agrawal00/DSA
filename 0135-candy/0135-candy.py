class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        
        candy = [1] * n
        for i in range(1,n):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        
        for i in range(n-2,-1,-1):
            if ratings[i+1 ] < ratings[i] :
                candy[i] = max(candy[i+1] + 1 , candy[i])
                
        return sum(candy)



        # specialcase if rearrangement is possible
        # n = len(ratings)
        # if n == 1:
        #     return 1
        # ratings.sort()
        # l = 0
        # r = n - 1
        # cnt = 0
        # while l < r:
        #     if ratings[l] < ratings[r]:
        #         cnt += 3
        #         l += 1
        #         r -= 1
        #     else :
        #         break
        # if l <= r:
        #     cnt += r - l + 1
        # return cnt