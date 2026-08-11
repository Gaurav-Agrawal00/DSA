class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans_set = set(nums)
        total_seq_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                total_seq_sum += nums[i]
            else:
                break
        
        while total_seq_sum in ans_set:
            total_seq_sum += 1
        
        return total_seq_sum