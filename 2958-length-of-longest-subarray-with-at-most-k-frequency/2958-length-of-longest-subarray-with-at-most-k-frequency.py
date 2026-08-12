class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hash_map = {}
        l = maxLen = 0
        for r in range(len(nums)):
            hash_map[nums[r]] = hash_map.get(nums[r] , 0) + 1
            while hash_map[nums[r]] > k:
                hash_map[nums[l]] -= 1
                l += 1
            
            maxLen = max(maxLen , r - l + 1)
        return maxLen