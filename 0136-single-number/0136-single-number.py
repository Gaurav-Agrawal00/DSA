class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash_map = {}
        # for i in range(len(nums)):
        #     hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        
        # for key,value in hash_map.items():
        #     if value == 1:
        #         return key
        # return -1

        result = 0
        for num in nums:
            result ^= num
        return result