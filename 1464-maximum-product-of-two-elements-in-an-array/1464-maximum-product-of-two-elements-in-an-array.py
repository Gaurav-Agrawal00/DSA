class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf')
        for num in nums:
            # for max element
            if num > max1 :
                max2 = max1 
                max1 = num
            elif num <= max1 and num > max2 :
                max2 = num
        
        return (max1 - 1) * (max2 - 1)
        