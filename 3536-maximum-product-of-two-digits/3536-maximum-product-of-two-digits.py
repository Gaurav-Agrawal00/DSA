class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        while n > 0:
            arr.append(n%10)
            n = n // 10
        
        max1 = 0
        max2 = 0
        for a in arr:
            if max1 < a:
                max2 = max1
                max1 = a 
            elif(max1 >= a and max2 < a):
                max2 = a
        
        return max1 * max2