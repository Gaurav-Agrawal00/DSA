class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # low = 0
        # mid = low + 1
        # high = len(arr) 
        # count = 0
        # while(mid<=high):
        #     if mid< high and arr[low]==arr[mid] :
        #         while arr[low] == arr[mid]:
        #             mid += 1
        #         arr[low + 1],arr[mid]=arr[mid],arr[low + 1]
        #         count += 1
        #         low += 1
        #     mid += 1 
        # return count


        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j+1