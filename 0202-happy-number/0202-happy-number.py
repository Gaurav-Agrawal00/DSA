class Solution:

    def isHappy(self, n: int) -> bool:
        isVisited = {}
        
        while n != 1:
            val = 0
            while n > 0:
                digit = n % 10
                val = val + digit * digit 
                n = n // 10
            if val in isVisited :
                return False
            
            isVisited[val] = 1
            n = val
        return True
