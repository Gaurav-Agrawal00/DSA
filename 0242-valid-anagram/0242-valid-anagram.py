class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def findFreq(a):    
            freq = {}
            for val in a:
                freq[val] = freq.get(val,0) + 1
            return freq
        
        freq1 = findFreq(s)
        freq2 = findFreq(t)
        if len(freq1) != len(freq2):
            return False
        
        for key in freq1:
            if key not in freq2 or freq1[key] != freq2[key] :
                return False
        return True