class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def findTotal(k):
            l = r = 0
            hash_map = {}
            cnt = 0
            while r < len(nums):
                hash_map[nums[r]] = hash_map.get(nums[r] , 0) + 1
                while len(hash_map) > k:
                    hash_map[nums[l]] -= 1
                    if hash_map[nums[l]] == 0:
                        del hash_map[nums[l]]
                    l = l+1
                if len(hash_map ) <= k:
                    cnt += r - l + 1
                r += 1
            return cnt
        return findTotal(k) - findTotal(k-1)