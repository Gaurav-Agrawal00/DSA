class Solution:

    def findParenthesis(self,s,open,close,n,ans):
        if len(s) == 2*n:
            ans.append(s)
            return 
        
        if open < n:
            self.findParenthesis(s + '(' , open + 1 , close , n , ans)
        
        if close < open :
            self.findParenthesis(s + ')' , open, close+1 , n , ans)
        

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.findParenthesis('',0,0,n,ans)
        return ans