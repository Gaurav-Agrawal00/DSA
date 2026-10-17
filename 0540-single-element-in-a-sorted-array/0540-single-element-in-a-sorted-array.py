class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1

        if len(arr)==1:
            return arr[0]
        if low == 0:
            if arr[low] != arr[low+1]:
                return arr[low]
            low += 1
        if high == len(arr)-1:
            if(arr[high]!= arr[high-1]):
                return arr[high]
            high -= 1
        
        while low<= high :
            mid = (low + high)//2
            if (arr[mid]!=arr[mid-1] and arr[mid ] != arr[mid + 1]):
                return arr[mid]
            else:
                if ((mid % 2 == 0 and arr[mid]==arr[mid+1]) or (arr[mid] == arr[mid-1] and mid % 2 == 1)):
                    low = mid + 1

                else:
                    high = mid - 1
        
