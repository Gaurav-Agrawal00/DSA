class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lMax = 0
        rMax = 0
        lMaxArr = [0] * n
        rMaxArr = [0] * n
        for i in range(n):
            lMax = max(lMax,height[i])
            rMax = max(rMax,height[n-1-i])
            lMaxArr[i] = lMax 
            rMaxArr[n-i-1] = rMax
        
        ans = 0
        for i in range(n):
            ans += (min(lMaxArr[i],rMaxArr[i])-height[i])
        return ans