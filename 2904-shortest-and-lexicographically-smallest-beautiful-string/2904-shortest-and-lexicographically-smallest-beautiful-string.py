class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        sIndex = -1
        l = r = 0
        cnt = 0
        minLen = float('inf')
        while r < len(s) :
            if s[r] =="1":
                cnt += 1
            while l < r and (cnt > k or s[l] == "0"):
                if s[l] == '1':
                    cnt -= 1
                l += 1 
            
            if cnt == k:
                if minLen > r - l + 1 :
                    minLen = r - l + 1 
                    sIndex =  l
                elif minLen == r - l + 1:    # most imp part for lexigraphic order.
                    if s[l : r+1] < s[sIndex : sIndex + minLen] :
                        sIndex = l
             
            r += 1
        return s[sIndex : sIndex + minLen] if sIndex >= 0 else ''