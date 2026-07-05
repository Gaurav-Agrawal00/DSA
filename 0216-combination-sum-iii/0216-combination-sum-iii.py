class Solution:
    def find(self,ind,k,target,ds,ans):
        if target == 0 and k == len(ds):
            ans.append(list(ds))
            return

        if len(ds) == k :
            return

        for i in range(ind,10):
            if i > target:
                break

            ds.append(i)

            self.find(i+1 , k , target - i , ds , ans)
            ds.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ds = []
        ans = []
        self.find(1,k,n,ds,ans)
        return ans