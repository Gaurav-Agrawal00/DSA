class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        length = 0
        hash_set = {}
        l = 0
        r = 0
        while r < len(s) :
            if s[r] in hash_set and hash_set[s[r]] >= l:
                l = hash_set[s[r]] + 1
            length = r - l + 1 
            max_len = max(max_len,length)
            hash_set[s[r]] = r
            r += 1
        return max_len
                
        # for i in range(len(s)):
        #     if s[i] in hash_set :
        #         length = length - hash_set[s[i]] + 1
        #         hash_set.pop(s[i])
                
            
        #     length += 1
        #     max_len = max(max_len,length)
        #     hash_set[s[i]] = i
        # return max_len

        # max_len = 0
        # for i in range(len(s)):
        #     hash_set = {}
        #     for j in range(i,len(s)):
        #         if s[j] in hash_set:
        #             break
                
        #         max_len = max(max_len,j-i+1)
        #         hash_set[s[j]] = 1
        # return max_len