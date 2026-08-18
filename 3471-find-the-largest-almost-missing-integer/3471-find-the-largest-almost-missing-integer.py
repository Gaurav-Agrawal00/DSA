class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len(nums) == k:
            return max(nums)
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num , 0) + 1
            
        if k == 1:
            ans = -1
            for key in freq:
                if freq[key] == 1:
                    ans = max(ans,key)
            return ans
        else:
            ans = -1
            if freq[nums[0]] == 1:
                ans = max(ans, nums[0])

            if freq[nums[n-1]] == 1:
                ans = max(ans, nums[n-1])

            return ans
