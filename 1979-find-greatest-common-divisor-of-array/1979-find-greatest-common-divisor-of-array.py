class Solution:

    def findGcd(self,a,b):
        while b!= 0:
            a,b = b, a%b
        return a
        
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        return self.findGcd(min_,max_)