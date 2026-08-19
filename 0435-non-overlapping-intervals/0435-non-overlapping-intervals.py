class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        endL = intervals[0][1]
        
        # intervals[1:] array ka ek tukda dega, index 1 se aakhiri tak
        for start, end in intervals[1:]:
            if start >= endL:
                endL = end
            else:
                cnt += 1
                endL = min(endL, end)
                
        return cnt