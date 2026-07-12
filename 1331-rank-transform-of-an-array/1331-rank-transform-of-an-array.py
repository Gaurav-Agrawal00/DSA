class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1 = list(arr)
        arr1.sort()
        
        hash_map = {}
        cnt = 1
        for num in arr1:
            if num not in hash_map:
                hash_map[num] = cnt
                cnt += 1
        
        ans = [hash_map[num] for num in arr]
        return ans