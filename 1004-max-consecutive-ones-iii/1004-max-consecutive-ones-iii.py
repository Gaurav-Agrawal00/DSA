class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        maxLen = 0
        cnt0= 0
        while r < len(nums):
            if nums[r] == 0:
                cnt0 += 1
            
            if cnt0 > k :
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            maxLen = max(maxLen,r-l+1)
            r+= 1
        return maxLen