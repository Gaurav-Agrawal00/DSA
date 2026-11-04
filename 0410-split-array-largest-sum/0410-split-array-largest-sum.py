class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def func(val):
            cnt = 1
            sum1 = 0
            for num in nums:
                sum1 += num
                if sum1 > val:
                    cnt+=1 
                    sum1 = num
            
            return cnt
        
        low = max(nums)
        high = sum(nums)
        while low <= high :
            mid = (low + high) //2 
            if func(mid) > k:
                low = mid + 1
            else:
                high = mid - 1
        return low