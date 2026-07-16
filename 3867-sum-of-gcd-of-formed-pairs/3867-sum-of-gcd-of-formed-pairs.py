class Solution:
    
    def findGcd(self,a,b):
        while b != 0 :
            a,b = b,a%b
        return a

    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        maxNum = 0
        for num in nums:
            maxNum = max(maxNum,num)
            prefixGcd.append(self.findGcd(num,maxNum))
        prefixGcd.sort()
        
        i = 0
        j = len(prefixGcd)-1
        n = 0
        while (i < j):
            n += self.findGcd(prefixGcd[i],prefixGcd[j])
            i += 1
            j -= 1
        return n