class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums :
            if max1 < num :
                max3 = max2
                max2 = max1
                max1 = num
            elif max1 >= num and max2 < num :
                max3 = max2 
                max2 = num 
            elif max2 >= num and max3 < num :
                max3 = num
            
            if min1 > num :
                min2 = min1
                min1 = num
            elif min1 <= num and min2 > num :
                min2 = num
                
        return max(max1 * max2 * max3 , max1*min1*min2)
       