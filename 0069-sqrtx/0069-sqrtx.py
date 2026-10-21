class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        if x == 0 or x == 1 :
            return x
        while low <= high :
            mid = (low + high ) // 2 
            dat = mid * mid
            if dat == x :
                return mid
            elif  dat > x:
                high = mid - 1
            else:
                low = mid + 1
            
        return high