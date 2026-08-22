class Solution:
    def checkDivisibility(self, n: int) -> bool:
        numS = 0
        numP = 1
        x = n
        while x > 0:
            numS = numS  + (x % 10)
            numP = numP * (x % 10)
            x = x //10

        return  n % (numS + numP )== 0 