class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        points1 = []
        points2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))
                if img2[r][c] == 1:
                    points2.append((r, c))
                    
        shift_count = {}
        max_overlap = 0
        
        for r1, c1 in points1:
            for r2, c2 in points2:
                shift = (r2 - r1, c2 - c1)
                
                if shift in shift_count:
                    shift_count[shift] += 1
                else:
                    shift_count[shift] = 1
                
                
                max_overlap = max(shift_count[shift],max_overlap)
                
        return max_overlap
