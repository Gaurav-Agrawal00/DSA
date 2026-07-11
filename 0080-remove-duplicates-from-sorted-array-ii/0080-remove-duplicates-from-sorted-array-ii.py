class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        j = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[j] and cnt == 2:
                continue
            elif nums[i] == nums[j]:
                j = j + 1
                cnt += 1
                nums[j] = nums[i]
            else:
                nums[j+1] = nums[i]
                j = j+1
                cnt = 1
        return j+1

        