class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        low = 0
        high = len(nums)-1 
        
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] >= target :
                high = mid - 1
                ans = mid
            else:
                low= mid + 1
        return ans