class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = -1
        b = -1
        c = -1
        cnt = 0

        for i in range(len(s)):
            if s[i] == 'a' :
                a = i
            elif s[i] == 'b':
                b = i
            else:
                c = i
            if a >= 0 and b >= 0 and c >= 0:
                cnt += 1 + min(a,b,c) 

        return cnt 