class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_range = 200
        for s in strs:
            min_range = min (min_range , len(s))
        
        ind = -1
        for i in range(min_range):
            isSame = True
            for j in range(len(strs)):
                if j > 0 and strs[j][i] != strs[j-1][i]:
                    isSame = False
                    break
                
            if isSame:
                ind = i
            else:
                break

        return strs[0][:ind+1]