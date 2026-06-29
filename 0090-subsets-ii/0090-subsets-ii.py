class Solution:
    def findSubsets(self,nums,ind,ans,ds):
        ans.append(list(ds))
        for i in range(ind,len(nums)):
            if ind < i and nums[i] == nums[i-1]:
                continue
            ds.append(nums[i])
            self.findSubsets(nums,i+1,ans,ds)
            ds.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ds= []
        ans = []
        self.findSubsets(nums,0,ans,ds)
        return ans