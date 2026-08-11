class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        net_xor = 0
        for i in range(len(nums)):
            net_xor ^= nums[i]

        final_diff = net_xor ^ k
        cnt = 0
        while final_diff > 0:
            if final_diff & 1 :
                cnt += 1
            final_diff = final_diff >> 1

        return cnt