class Solution:
    def findPeakGrid(self, arr: List[List[int]]) -> List[int]:
        l1 = 0
        n = len(arr)
        h1 = n-1
        while(l1<= h1):
            m1 = (l1+h1)//2
            index  = -1
            max_el = -1
            for i in range(len(arr[0])):
                if max_el < arr[m1][i]:
                    max_el = arr[m1][i]
                    index = i
            if len(arr)==1:
                return [m1,index]
            elif(m1 == 0 and arr[m1][index] > arr[m1+1][index]):
                return [m1,index]
            elif(m1 == n-1 and arr[m1][index] > arr[m1-1][index]):
                return [m1,index]
            elif(arr[m1][index] > arr[m1+1][index] and arr[m1][index] > arr[m1-1][index]):
                return [m1,index]
            elif(arr[m1][index] < arr[m1+1][index]):
                l1 = m1+1
            elif(arr[m1][index] < arr[m1-1][index]):
                h1 = m1-1
            else:
                h1 = m1-1
        return [-1,-1]

            