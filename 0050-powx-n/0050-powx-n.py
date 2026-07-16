class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = n
        if n < 0 :
            power = power * -1 
        ans = 1
        while power > 0:
            if power % 2 == 1:
                ans = ans * x
                power = power - 1
            else:
                x = x * x
                power = power // 2 
        if n > 0 :
            return ans
        else:
            return 1 / ans
