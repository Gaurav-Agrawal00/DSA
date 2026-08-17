class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)-1
        if n == 0 :
            return 0

        l = 0
        r = n

        lMax = 0
        rMax = 0
        ans = 0

        while l < r :
            if height[l] <= height[r] :
                if height[l] >= lMax :
                    lMax = height[l] 
                else:
                    ans += lMax - height[l] 
                l += 1
            else:
                if height[r] >= rMax :
                    rMax = height[r]
                else:
                    ans += rMax - height[r]
                r -= 1
        return ans



        # n = len(height)
        # lMax = 0
        # rMax = 0
        # lMaxArr = [0] * n
        # rMaxArr = [0] * n
        # for i in range(n):
        #     lMax = max(lMax,height[i])
        #     rMax = max(rMax,height[n-1-i])
        #     lMaxArr[i] = lMax 
        #     rMaxArr[n-i-1] = rMax
        
        # ans = 0
        # for i in range(n):
        #     ans += (min(lMaxArr[i],rMaxArr[i])-height[i])
        # return ans