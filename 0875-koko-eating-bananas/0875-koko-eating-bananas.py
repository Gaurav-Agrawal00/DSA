class Solution:
    def func(self,piles,mid):
        val = 0
        for pile in piles:
            val += (pile + mid -1)//mid
        return val

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max_val = float('-inf')
        # for val in piles:
        #     max_val = max(max_val,val)
            
        max_val = max(piles)

        low = 1
        high = max_val
        
        while(low <= high):
            mid = (low + high)//2

            if (self.func(piles,mid) <= h):
                high = mid - 1
            else:
                low = mid + 1

        return low