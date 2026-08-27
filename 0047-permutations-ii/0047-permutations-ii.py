class Solution:
    def findPer(self,ind,nums,ans,n):
        if ind == n:
            ans.add(tuple(nums[:]))
        
        for i in range(ind,n):
            nums[i] , nums[ind] = nums[ind] , nums[i]
            self.findPer(ind+1 , nums,ans,n)
            nums[i] , nums[ind] = nums[ind] , nums[i]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.findPer(0,nums,ans,len(nums))
        return list(ans)