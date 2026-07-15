class Solution:

    def findGcd(self,a,b):
        while b != 0 :
            a , b = b , a%b
        return a



    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = 0
        even = 0
        for i in range(n):
            odd = odd + 2* i + 1
            even = 2 * i + 2 + even 
        
        # len1 = min(odd,even)+1
        # value = 0
        # for i in range(1, len1):
        #     if odd % i == 0 and even % i == 0 :
        #         value = i
        
        # self.findGcd(odd,even)

        return self.findGcd(odd,even)
    