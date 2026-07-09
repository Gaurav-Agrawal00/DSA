class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        i = 0
        while i <= last:
            if nums[i] == val:
                while last >= 0 and nums[last] == val:
                    last -= 1

                if i > last:
                    break
                nums[i] = nums[last]
                last -= 1
            i += 1
        return last + 1
