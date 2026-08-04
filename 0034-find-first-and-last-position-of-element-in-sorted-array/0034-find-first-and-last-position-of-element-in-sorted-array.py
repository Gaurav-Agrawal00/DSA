class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        if len(arr) == 0:
            return [-1,-1]
        n = len(arr)-1
        low = 0
        high = n
        ans1 = -1
        while low <= high :
            mid = (low + high)//2
            if arr[mid] >= target:
                ans1 = mid
                high = mid - 1
            else:
                low = mid + 1
        if ans1 == -1 :
            return [-1,-1]
        ans2 = -1
        low = 0
        high = n
        while low <= high :
            mid = (low + high)//2
            if arr[mid] <= target :
                ans2 = mid
                low  = mid + 1
            else:
                high = mid - 1
        
        if arr[ans1] == target :
            return [ans1,ans2]
        else:
            return [-1,-1]