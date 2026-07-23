class Solution:

    # def findXorTriplet(self,ind,nums,ans,ds,cnt):
    #     if cnt == 3:
    #         ans.add(ds)
    #         return
        
    #     if ind == len(nums):
    #         return

    #     for i in range(ind,len(nums)):
    #         cnt += 1
    #         ds = ds ^ nums[i]
    #         self.findXorTriplet(i,nums,ans,ds,cnt)
    #         ds = ds ^ nums[i]
    #         cnt -= 1

    # def uniqueXorTriplets(self, nums: List[int]) -> int:
    #     ans = set()
    #     ds = 0
    #     cnt = 0
    #     self.findXorTriplet(0,nums,ans,ds,cnt)
    #     return len(ans)

    # def uniqueXorTriplets(self, nums: List[int]) -> int:
    #     ansSet = set()
    #     xor = 0
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i,n):
    #             xor = nums[i] ^ nums[j]
    #             for k in range(j,n):
    #                 ansSet.add(xor^nums[k])

    #     return len(ansSet)

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3 :
            return n
        
        return 1 << n.bit_length()