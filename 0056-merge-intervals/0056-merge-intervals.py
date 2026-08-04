class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        # ans array mein seedha pehla interval daal do
        ans = [intervals[0]]
        
        # Loop 2nd element (index 1) se shuru karenge
        for i in range(1, len(intervals)):
            
            # CHECK OVERLAP: Agar current ka starting point, 'ans' ke aakhiri element ke end point se chota ya barabar hai
            if intervals[i][0] <= ans[-1][1]:
                
                # Overlap hai! Toh 'ans' ke aakhiri element ka end point update kar do (max lekar)
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
                
            else:
                # Overlap NAHI hai! Toh seedha naya interval 'ans' mein push kar do
                ans.append(intervals[i])
                
        return ans