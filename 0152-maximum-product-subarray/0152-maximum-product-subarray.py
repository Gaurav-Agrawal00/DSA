class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        sufix = 1
        maxAns = float('-inf')
        n = len(nums)
        for i in range(n):
            prefix *= nums[i]
            sufix *= nums[n-i-1]

            maxAns = max(maxAns,prefix,sufix)

            if prefix == 0:
                prefix = 1
            if sufix == 0:
                sufix = 1
        return maxAns