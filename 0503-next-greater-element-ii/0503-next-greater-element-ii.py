class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * size
        stack = []
        for i in range(2*len(nums)-1,-1,-1):
            if i < size:
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                
                if stack :
                    ans[i] = stack[-1]
                else:
                    ans[i] = -1
                stack.append(nums[i])
            else:
                ind = i % len(nums)
                while stack and nums[ind] >= stack[-1]:
                    stack.pop()
                stack.append(nums[ind])
        return ans
