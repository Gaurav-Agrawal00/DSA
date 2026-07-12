class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1 = list(arr)
        arr1.sort()
        
        hash_map = {}
        cnt = 1
        for i in range(len(arr)):
            if arr1[i] not in hash_map:
                hash_map[arr1[i]] = hash_map.get(arr1[i],cnt)
                cnt += 1
        
        ans = [0]* len(arr)

        for i in range(len(arr)):
            ans[i] = hash_map[arr[i]]
        return ans