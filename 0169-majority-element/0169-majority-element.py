class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        cnt = 0
        for num in nums :
            if num == val :
                cnt += 1
            else:
                cnt -= 1

            if cnt <= 0 :
                val = num
                cnt = 1
        return val
