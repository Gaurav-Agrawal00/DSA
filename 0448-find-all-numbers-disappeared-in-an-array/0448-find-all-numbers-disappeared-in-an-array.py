class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            x = nums[i]
            x = abs(x)
            if nums[x-1] > 0:
                nums[x-1] = -1 * nums[x-1]
        
        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)
        return ans