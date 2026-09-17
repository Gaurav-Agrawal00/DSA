class Solution:
    def findCombination(self,arr,ind,target,ans,ds):
        if target == 0:
            ans.append(list(ds))
            return
        
        for i in range(ind,len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue
            if arr[i]>target:
                break
            
            ds.append(arr[i])
            self.findCombination(arr,i+1,target-arr[i],ans,ds)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans= []
        ds= []
        self.findCombination(candidates,0,target,ans,ds)
        return ans