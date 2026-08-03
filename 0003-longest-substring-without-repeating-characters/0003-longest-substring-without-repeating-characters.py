class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            hash_set = {}
            for j in range(i,len(s)):
                if s[j] in hash_set:
                    break
                
                max_len = max(max_len,j-i+1)
                hash_set[s[j]] = 1
        return max_len