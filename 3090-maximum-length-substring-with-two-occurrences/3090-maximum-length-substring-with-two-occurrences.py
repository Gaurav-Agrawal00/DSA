class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash_map = {}
        l = maxLen = 0
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0 ) + 1
            while hash_map[s[i]] > 2:
                hash_map[s[l]] -= 1
                l += 1
            maxLen = max(maxLen,i-l+1)
        return maxLen