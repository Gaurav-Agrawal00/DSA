class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        n = rowIndex + 1
        val =  1
        ans.append(val)
        for i in range(1,n):
            val = val * (n-i)
            val = val // (i)
            ans.append(val)
        return ans