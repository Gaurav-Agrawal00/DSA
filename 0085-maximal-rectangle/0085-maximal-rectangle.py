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
            maxi = max(maxi,int((nse[i]-pse[i]-1)*heights[i])) 

        return maxi
    

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        prefixSum = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    temp.append(0)
                    continue
                if i != 0 :
                    temp.append(prefixSum[i-1][j] + 1)
                else:
                    temp.append(1)
            prefixSum.append(temp)
        ans = []
        for i in range(len(matrix)):
            ans.append(self.largestRectangleArea(prefixSum[i]))
        return max(ans)