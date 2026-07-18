class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 :
            return x
        isPos = True
        if x < 0 :
            isPos = False
            x = -x
        
        val = 0
        while x > 0 :
            val = val * 10 + x % 10 
            x = x // 10
        ans = val if isPos else -val

        if ans > 2**31-1 or ans < -2**31:
            return 0
        return ans
