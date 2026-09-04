class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        
        
        suffix_min = [0] * N
        min_val = float('inf')
        for i in range(N - 1, -1, -1):
            min_val = min(min_val, nums[i])
            suffix_min[i] = min_val
            
       
        max_val = float('-inf')
        for i in range(N):
            max_val = max(max_val, nums[i])
            
            if (max_val - suffix_min[i]) <= k:
                return i
                
        return -1