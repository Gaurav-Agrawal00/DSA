class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:

            temp = n
            prev = 1 
            while temp > 0:
                prev = prev * (temp % 10)
                temp = temp // 10
            
            if prev % t == 0:
                return n 
            n+= 1