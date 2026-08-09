class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt1 = 0
        l = r = 0
        val = 0
        while r < len(nums) :
            val += nums[r]
            while val > goal and l <= r :
                val -= nums[l]
                l += 1
            
            if val <= goal :
                cnt1 += r - l + 1
            r += 1

        cnt2 = 0
        l = r = 0
        val = 0
        while r < len(nums) :
            val += nums[r]
            while val > goal-1 and l <= r :
                val -= nums[l]
                l += 1
            
            if val <= (goal - 1):
                cnt2 += r - l + 1
            r += 1
        print(cnt1,cnt2)
        return cnt1 - cnt2
