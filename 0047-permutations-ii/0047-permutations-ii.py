class Solution:
    def findPer(self, ind, nums, ans, n):
        if ind == n:
            ans.append(nums[:])
            return 
        
        # This set keeps track of the numbers we've swapped into 'ind' 
        # for THIS specific depth of the recursion tree.
        seen = set()
        
        for i in range(ind, n):
            if nums[i] in seen:
                continue # Skip this branch, we've already done this number
            
            seen.add(nums[i])
            
            nums[i], nums[ind] = nums[ind], nums[i]
            self.findPer(ind + 1, nums, ans, n)
            nums[i], nums[ind] = nums[ind], nums[i]

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = [] # We can go back to using a normal list now!
        self.findPer(0, nums, ans, len(nums))
        return ans