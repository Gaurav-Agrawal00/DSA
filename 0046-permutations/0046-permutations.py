class Solution:
    def findPer(self,ind,nums,ans,n):
        if ind == n :
            ans.append(nums[:])
            return 
        
        for i in range(ind,n):
            nums[i] , nums[ind] = nums[ind] , nums[i]
            self.findPer(ind+1,nums,ans,n)
            nums[i] , nums[ind] = nums[ind] , nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.findPer(0,nums,ans,len(nums))
        return ans