# class Solution:

#     def findGcd(self,a,b):
#         while b != 0 :
#             a,b = b,a%b
#         return a

#     def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
#         gcdPairs = []
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 gcdPairs.append(self.findGcd(nums[i],nums[j]))
        
#         gcdPairs.sort()

#         for i in range(len(queries)):
#             queries[i] = gcdPairs[queries[i]]

#         return queries

class Solution:
    # 1. Bina kisi import ke apna Binary Search banao
    def myBinarySearch(self, arr: list[int], target: int) -> int:
        low = 0
        high = len(arr)
        
        while low < high:
            mid = (low + high) // 2
            # Agar mid ki value target ke barabar ya choti hai, 
            # toh hum aage (right side) dhundenge
            if arr[mid] <= target:
                low = mid + 1
            else:
                # Warna pichhe (left side) aayenge
                high = mid
                
        return low

    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        count_gcd = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            multiples = 0
            for m in range(g, max_val + 1, g):
                multiples += freq[m]
            pairs = multiples * (multiples - 1) // 2
            for m in range(2 * g, max_val + 1, g):
                pairs -= count_gcd[m]
            count_gcd[g] = pairs
            
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + count_gcd[i]
            
        # 2. Yahan import ki jagah apna myBinarySearch call karo!
        ans = []
        for q in queries:
            idx = self.myBinarySearch(prefix, q)
            ans.append(idx)
            
        return ans