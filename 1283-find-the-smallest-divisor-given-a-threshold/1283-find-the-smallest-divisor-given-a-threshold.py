class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def func(mid):
            return sum(math.ceil(i / mid) for i in nums)
        
        low = 1
        high = max(nums)
        ans = -1
        while low <= high :
            mid = (low + high ) // 2
            if func(mid) <= threshold :
                high = mid - 1
            else:
                low = mid + 1
        return low
