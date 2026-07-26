from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        q = deque()
        for i in range(len(nums)):

            if q and q[0] == i-k:
                q.popleft()
            
            while q and nums[q[-1]] <= nums[i] :
                q.pop()

            q.append(i)

            if i >= k-1:
                ans.append(nums[q[0]])

        return ans
        # brute in o(n*k) time complexity
        # n = len(nums)
        # if n <= k:
        #     return [max(nums)]
        
        # ans = []
        # for i in range(len(nums)-k+1):
        #     maxi = float('-inf')
        #     for j in range(i,i+k):
        #         maxi = max(maxi,nums[j])
        #     ans.append(maxi)
        # return ans
