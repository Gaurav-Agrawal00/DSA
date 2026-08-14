class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minL = float('-inf')
        maxL = float('inf')
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < target:
                    minL = max(minL , val)
                    l += 1
                else:
                    maxL = min(maxL , val)
                    r -= 1
        return minL if (maxL - target) > (target - minL) else maxL 