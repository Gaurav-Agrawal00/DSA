class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def findGoal(goal):
            if goal < 0 :
                return 0
            cnt1 = 0
            l = r = 0
            val = 0
            while r < len(nums) :
                val += nums[r] % 2
                while val > goal and l <= r :
                    val -= nums[l] % 2
                    l += 1
                
                cnt1 += r - l + 1
                r += 1
            return cnt1

        return findGoal(k) - findGoal(k-1)