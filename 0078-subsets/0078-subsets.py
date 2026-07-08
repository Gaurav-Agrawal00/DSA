class Solution:

    # def findSubsets(self,ind,arr,ans,ds):
    #     if ind == len(arr) :
    #         ans.append(list(ds))
    #         return
        
    #     ds.append(arr[ind])
    #     self.findSubsets(ind+1,arr,ans,ds)
    #     ds.pop()

    #     self.findSubsets(ind+1,arr,ans,ds)

        


    def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     ds = []
    #     self.findSubsets(0,nums,ans,ds)
    #     return ans

        n = len(nums)
        subsets = 1 << n
        ans = []
        for num in range(subsets):
            ds = []
            for j in range(n):
                if num & (1<<j) :
                    ds.append(nums[j])
            ans.append(ds)
        return ans 