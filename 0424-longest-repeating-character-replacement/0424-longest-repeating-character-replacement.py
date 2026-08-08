class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        max_freq = 0
        l = 0 
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i] , 0) + 1
            max_freq = max (max_freq , hash_map[s[i]])
            if (i-l+1) - max_freq > k:
                hash_map[s[l]] -= 1
                l += 1
            maxLen = max(maxLen , i - l + 1)
        return maxLen