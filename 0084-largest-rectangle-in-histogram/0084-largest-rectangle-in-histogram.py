class Solution:
    def findNse(self,arr,n):
        stack = []
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack :
                ans[i] = stack[-1]
            else:
                ans[i] = n
            stack.append(i)
        return ans

    def findPse(self,arr,n):
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack :
                ans[i] = stack[-1]
            else:
                ans[i] = -1
            stack.append(i)
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = self.findNse(heights,n)
        pse = self.findPse(heights,n)

        maxi = 0
        for i in range(n):
            maxi = max(maxi,(nse[i]-pse[i]-1)*heights[i]) 

        return maxi
        