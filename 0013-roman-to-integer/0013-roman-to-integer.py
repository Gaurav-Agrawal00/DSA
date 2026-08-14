class Solution:
    def romanToInt(self, s: str) -> int:
        romanSet = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50 , "C" : 100 , "D" : 500 , "M" : 1000}
        i = ans = 0
        while i < len(s):
            if i < len(s)-1 and romanSet[s[i]] < romanSet[s[i+1]]:
                ans += romanSet[s[i+1]] - romanSet[s[i]]
                i += 2
            else:
                ans+= romanSet[s[i]]
                i += 1
        # if romanSet[s[len(s)-1]] <= romanSet[s[len(s)-2]]:
        #     ans += romanSet[s[i]]
        return ans