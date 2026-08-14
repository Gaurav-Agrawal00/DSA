class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        r = len(height)-1
        maxAr = 0
        while i < r:
            maxAr = max(maxAr , (min(height[r],height[i]) * (r - i)))
            if height[i] > height[r]:
                r -= 1
            else:
                i+= 1
        return maxAr