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
        # if romanSet[s[len(s)-1]] <= romanSet[s[len(s)-2]]:    #ye ek aur error ka krn ho skta h agr ek  hhi elem h toh yer don oko le lega qki -1 bole toh last index or 2 baar jod dega
        #     ans += romanSet[s[i]]
        return ans