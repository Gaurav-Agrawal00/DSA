class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1

        if dividend == -2**31 and divisor == -1:
            return 2**31-1

        if divisor == 1:
            return dividend
        
        isPos = True
        if divisor > 0 and dividend < 0 :
            isPos = False
        if divisor < 0 and dividend > 0:
            isPos = False
        
        quot = abs(dividend)
        div = abs(divisor)

        # total = 0
        # cnt = 0
        # while total + div <= quot:
        #     cnt += 1
        #     total += div
        
        ans = 0
        while quot >= div :
            cnt = 0
            while quot >= (div<<(cnt+1)):
                cnt += 1
            ans += (1 << cnt)
            quot = quot - (div << cnt)

        if ans > 2**31-1 and isPos :
            return float('inf')

        if ans > (2)**31 and not isPos :
            return float('-inf')
        
        if isPos :
            return ans
        else:
            return -ans
