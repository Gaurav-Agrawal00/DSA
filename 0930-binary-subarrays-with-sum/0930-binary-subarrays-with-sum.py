class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            # Edge Case: Agar sum negative dhoondhna hai, par numbers sirf 0/1 hain
            if k < 0:
                return 0
                
            l = 0
            val = 0
            cnt = 0
            
            for r in range(len(nums)):
                # 1. Naye number ko window mein jodo
                val += nums[r]
                
                # 2. Agar window ka sum limit (k) se bada ho gaya, toh pichhe se chota karo
                # Tumhari galti yahin thi: tumne k ki jagah goal likh diya tha
                while val > k and l <= r:
                    val -= nums[l]
                    l += 1
                    
                # 3. Valid window ke subarrays count karo
                cnt += r - l + 1
                
            return cnt

        # AAPKA WALA MATH FORMULA: Exact(goal) = AtMost(goal) - AtMost(goal - 1)
        return atMost(goal) - atMost(goal - 1)