class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def findGoal(goal):
            if goal < 0 :
                return 0
            cnt1 = 0
            l = r = 0
            val = 0
            while r < len(nums) :
                val += nums[r]
                while val > goal and l <= r :
                    val -= nums[l]
                    l += 1
                
                cnt1 += r - l + 1
                r += 1
            return cnt1


        return findGoal(goal) - findGoal(goal-1)
