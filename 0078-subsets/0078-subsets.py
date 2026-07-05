class Solution:

    def findSubsets(self,ind,arr,ans,ds):
        if ind == len(arr) :
            ans.append(list(ds))
            return
        
        ds.append(arr[ind])
        self.findSubsets(ind+1,arr,ans,ds)
        ds.pop()

        self.findSubsets(ind+1,arr,ans,ds)

        


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        self.findSubsets(0,nums,ans,ds)
        return ans