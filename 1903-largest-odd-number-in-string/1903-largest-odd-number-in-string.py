class Solution:
    def largestOddNumber(self, num: str) -> str:
        ind = -1
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                ind = i
                break
        
        return num[ : ind + 1] if ind >= 0 else ""