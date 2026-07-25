class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = 0
        max2 = 0
        while n > 0:
            if max1 < n%10:
                max2 = max1
                max1 = n%10 
            elif(max1 >= n%10 and max2 < n%10):
                max2 = n%10
            n = n // 10            
        
        return max1 * max2