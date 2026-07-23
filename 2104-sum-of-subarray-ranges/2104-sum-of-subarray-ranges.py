class Solution:

    def findPse(self,arr):
        ans = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack :
                ans[i] = stack[-1]
            else:
                ans[i] = -1
            stack.append(i)
        return ans

    def findNse(self,arr):
        ans = [0] * len(arr)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack :
                ans[i] = stack[-1]
            else:
                ans[i] = len(arr)
            stack.append(i)
        return ans

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.findNse(arr)
        pse = self.findPse(arr)
        ans = 0
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i

            ans = (ans + (left*right*arr[i]))
        return ans
    
    def findPme(self,arr):
        ans = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            
            if stack :
                ans[i] = stack[-1]
            else:
                ans[i] = -1
            stack.append(i)
        return ans

    def findNme(self,arr):
        ans = [0] * len(arr)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            if stack :
                ans[i] = stack[-1]
            else:
                ans[i] = len(arr)
            stack.append(i)
        return ans

    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        nse = self.findNme(arr)
        pse = self.findPme(arr)
        ans = 0
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i

            ans = (ans + (left*right*arr[i]))
        return ans

    def subArrayRanges(self, nums: List[int]) -> int:
        maxSm = self.sumSubarrayMaxs(nums)
        minSm = self.sumSubarrayMins(nums)
        return maxSm - minSm 