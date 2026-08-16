class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxInd =  0
        for i in range(len(nums)):
            if maxInd < i :
                return False
            val = i + nums[i]
            maxInd = max(maxInd , val)
            if maxInd >= len(nums) - 1:
                return True
        return False
