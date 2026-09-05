class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev1 = 0
        prev2 = 1

        for i in range(2,n+1):
            prev2 , prev1 = prev2 + prev1 , prev2
        return prev2