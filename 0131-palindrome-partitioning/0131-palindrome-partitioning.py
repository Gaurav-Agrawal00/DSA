class Solution:

    def isPallindrome(self,start,end,s):
        while start <= end :
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def func(self,s,ind,ans,ds):
        if ind == len(s):
            ans.append(list(ds))
            return
        
        for i in range(ind,len(s)):
            if self.isPallindrome(ind,i,s):
                ds.append(s[ind:i+1])
                self.func(s,i+1,ans,ds)
                ds.pop()


    def partition(self, s: str):
        #your code goes here
        ans = []
        ds = []
        self.func(s,0,ans,ds)
        return ans