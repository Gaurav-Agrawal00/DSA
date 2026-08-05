class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxAns = 0
        cnt0 = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt0 += 1
            
            while cnt0 > k:
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            
            maxAns = max(maxAns,r-l+1)
        return maxAns