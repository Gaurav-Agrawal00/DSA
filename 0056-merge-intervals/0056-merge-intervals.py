class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        x = intervals[0][0]
        y = intervals[0][1]
        ans = []
        for i in range(n):
            if intervals[i][0] <= y:
                if intervals[i][1] > y:
                    y = intervals[i][1]
            else:
                ans.append([x,y])
                x = intervals[i][0]
                y = intervals[i][1]

        ans.append([x,y])
        return ans