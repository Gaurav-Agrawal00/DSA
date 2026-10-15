class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            data_set = set()
            val = 0
            for j in range(i,len(nums)):
                data_set.add(nums[j])
                val = len(data_set)
                ans += val * val
        return ans
