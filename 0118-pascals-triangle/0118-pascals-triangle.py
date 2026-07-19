class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if i == j or j == 0:
                    temp.append(1) 
                else:
                    temp.append(ans[i-1][j]+ans[i-1][j-1])
            ans.append(temp)
        return ans    
                